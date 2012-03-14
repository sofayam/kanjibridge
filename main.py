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

import mergeinput

import logging

class MainHandler(webapp.RequestHandler):
    def get(self):

        ks = Kanji.all().fetch(10)
        for k in ks:
            self.response.out.write(k.meaning)
        self.response.out.write("finished")

class Initialise(webapp.RequestHandler):
    def get(self):
        rawDict = mergeinput.merge()
        for idx in rawDict.keys():
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
            path = os.path.join(os.path.dirname(__file__), 'readings.html')
            template_values = {
                'glyph': kanji.glyph,
                'on': kanji.on,
                'kun': kanji.kun,
                'nextidx': idx+1
                }
            self.response.out.write(template.render(path, template_values))
        else:
            self.response.out.write("nothing found for idx %d" % idx)  

class Map(webapp.RequestHandler):
    def get(self):
        ks = Kanji.all().fetch(1000)
        hw = []
        for k in ks:
            q = db.Query(Word)
            q.filter("kanjis =", k.glyph)
            if q.get():
                logging.debug("Found word using %s" % k.glyph)
                hw.append(k)
                k.color = "red"
            else:
                k.color = "black"
                logging.debug("No words using %s" % k.glyph)

        path = os.path.join(os.path.dirname(__file__), 'map.html')
        template_values = {
            'kanjis': ks,
            'hasWord': hw
            }
        self.response.out.write(template.render(path, template_values))


class LogSenderHandler(InboundMailHandler):
    def receive(self,mail_message):
        logging.debug("Recv. message from " + mail_message.sender)
        for content_type, body in mail_message.bodies('text/plain'):
            btext = body.decode()
            # logging.debug("Body is >>" + btext)
            for item in btext.split("\n\n"):
                spl = item.split("\n")
                if len(spl) == 2:
                    (jap,eng) = spl
                    logging.debug("Found eng %s and jap %s" % (eng,jap)) 
                    #m = re.match(r"(\w+) \((\w+)\).*",jap)
                    m = re.match(ur"(\w+)\uff08(\w+)\uff09",jap,re.UNICODE)
                    if m:
                        g =  m.groups()
                        if len(g) == 2:
                            k,p = g
                            logging.debug("Kanji %s, Kana %s" % (k,p))
                            dbClasses.makeWord(k,p,eng)
                            #w = Word()
                            #w.kaki = k
                            #w.yomi = p
                            #w.meaning = eng
                            #w.put()
                    else:
                        logging.debug("No match for >%s<",jap)
                
            
            
        
def main():
    logging.getLogger().setLevel(logging.DEBUG)
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/init', Initialise),
                                          ('/keyword', QKeyword),
                                          ('/kanji', QKanji),
                                          ('/readings', QReadings),
                                          ('/map', Map),
                                          LogSenderHandler.mapping()],
                                         debug=True)
    run_wsgi_app(application)


if __name__ == '__main__':
    main()
