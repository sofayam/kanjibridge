#!/usr/bin/env python
#
import os
import re

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler

from dbClasses import Kanji
from dbClasses import Word
import dbClasses

import urllib
from google.appengine.api import urlfetch
import mergeinput


from django.utils import simplejson as json


import logging

class MainHandler(webapp.RequestHandler):
    def get(self):
        # TODO decent start page with useful links
        ks = Kanji.all().fetch(10)
        for k in ks:
            self.response.out.write(k.meaning)
        self.response.out.write("finished")

class Initialise(webapp.RequestHandler):
    def get(self):
        startraw = self.request.get('start')
        if startraw:
            start = int(startraw)
        else:
            start = 1

        rawDict = mergeinput.merge()
        for idx in sorted(rawDict.keys()):
            if idx < start: continue
            rk = rawDict[idx]
            k = Kanji()
            k.idx = rk['idx']
            k.keyword = unicode(rk['keyword'],encoding="utf-8")
            k.glyph = unicode(rk['glyph'],encoding="utf-8")
            k.meaning = unicode(rk['meaning'],encoding="utf-8")
            k.on = unicode(rk['on'],encoding="utf-8")
            k.kun = unicode(rk['kun'],encoding="utf-8")
            k.put()
        self.redirect('/')

class QKeyword(webapp.RequestHandler):
    def get(self):
        q = db.Query(Kanji)
        idx = int(self.request.get('idx'))
        q.filter("idx =", idx)
        kanji = q.get()
        if kanji:
            path = os.path.join(os.path.dirname(__file__), 'keyword.html')
            template_values = {
                'idx': kanji.idx,
                'keyword': kanji.keyword
                }
            self.response.out.write(template.render(path, template_values))
        else:
            self.response.out.write("nothing found for idx %d" % idx)  
      
class QKanji(webapp.RequestHandler):
    def get(self):
        q = db.Query(Kanji)
        idx = int(self.request.get('idx'))
        q.filter("idx =", idx)
        kanji = q.get()
        if kanji:
            path = os.path.join(os.path.dirname(__file__), 'kanji.html')
            template_values = {
                'glyph': kanji.glyph,
                'meaning': kanji.meaning,
                'idx': idx
                }
            self.response.out.write(template.render(path, template_values))
        else:
            self.response.out.write("nothing found for idx %d" % idx)  

class QReadings(webapp.RequestHandler):
    def get(self):
        q = db.Query(Kanji)
        idx = int(self.request.get('idx'))
        q.filter("idx =", idx)
        kanji = q.get()
        if kanji:
            q2 = db.Query(Word)
            q2.filter("kanjis =", kanji.glyph)
            words = q2.fetch(10)
            path = os.path.join(os.path.dirname(__file__), 'readings.html')
            template_values = {
                'kanji': kanji,
                'words': words,
                'nextidx': idx+1
                }
            self.response.out.write(template.render(path, template_values))
        else:
            self.response.out.write("nothing found for idx %d" % idx)  

class QWords(webapp.RequestHandler):
    def get(self):
        q1 = db.Query(Kanji)
        idx = int(self.request.get('idx'))
        q1.filter("idx =", idx)
        kanji = q1.get()
        if kanji:
            q2 = db.Query(Word)
            q2.filter("kanjis =", kanji.glyph)
            words = q2.fetch(10)
            path = os.path.join(os.path.dirname(__file__), 'words.html')
            template_values = {
                'kanji': kanji,
                'words': words,
                }
            self.response.out.write(template.render(path, template_values))
        else:
            self.response.out.write("nothing found for idx %d" % idx)  

class Map(webapp.RequestHandler):
    def get(self):
        ctraw = self.request.get('ct')
        if ctraw:
            ct = int(ctraw)
        else:
            ct = 100
        ks = Kanji.all().fetch(ct)
        for k in ks:
            q = db.Query(Word)
            q.filter("kanjis =", k.glyph)
            if q.get():
                #logging.debug("Found word using %s" % k.glyph)
                k.color = "red"
            else:
                k.color = "black"
                #logging.debug("No words using %s" % k.glyph)

        path = os.path.join(os.path.dirname(__file__), 'map.html')
        template_values = {
            'kanjis': ks,
            }
        self.response.out.write(template.render(path, template_values))


class LogSenderHandler(InboundMailHandler):
    def receive(self,mail_message):
        logging.debug("Recv. message from " + mail_message.sender)
        for content_type, body in mail_message.bodies('text/plain'):
            btext = body.decode()
            logging.debug("Body is >>" + btext)
            payload = {}
            payload['subject'] = mail_message.subject
            payload['body'] = btext.split("\n\n")
            url = "http://54.247.111.190:8080/wordimpex"
            #url = "http://localhost:8080/wordimpex"
            result = urlfetch.fetch(url = url, 
                                    payload = json.dumps(payload), 
                                    method = urlfetch.POST,
                                    headers = {'Content-Type': 'text/json'})

            logging.debug("returned from urlfetch")
                              
            return
            for item in btext.split("\n\n"):
                spl = item.split("\n")
                #logging.debug("Split the item")
                if len(spl) == 2:
                    (jap,eng) = spl
                    eng = eng[0:500]
                    #logging.debug("Found eng %s and jap %s" % (eng,jap)) 
                    #m = re.match(r"(\w+) \((\w+)\).*",jap)
                    m = re.match(ur"(\w+)\uff08(\w+)\uff09",jap,re.UNICODE)
                    if m:
                        g =  m.groups()
                        if len(g) == 2:
                            k,p = g
                            #logging.debug("Kanji %s, Kana %s" % (k,p))
                            dbClasses.makeWord(k,p,eng)
                            #w = Word()
                            #w.kaki = k
                            #w.yomi = p
                            #w.meaning = eng
                            #w.put()
                    else:
                        logging.debug("No match for >%s<",jap)
                else:
                    logging.debug("item could not be split>%s<",item)
                
            
            
        
def main():
    logging.getLogger().setLevel(logging.DEBUG)
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/init', Initialise),
                                          ('/keyword', QKeyword),
                                          ('/kanji', QKanji),
                                          ('/readings', QReadings),
                                          ('/words', QWords),
                                          ('/map', Map),
                                          LogSenderHandler.mapping()],
                                         debug=True)
    run_wsgi_app(application)


if __name__ == '__main__':
    main()
