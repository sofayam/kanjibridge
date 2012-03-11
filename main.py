#!/usr/bin/env python
#
import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from google.appengine.api import users
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db


import mergeinput

class Kanji(db.Model):
    idx = db.IntegerProperty()
    keyword = db.StringProperty()
    glyph = db.StringProperty()
    meaning = db.StringProperty()
    on = db.StringProperty()
    kun = db.StringProperty()


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
                'meaning': kanji.meaning
                }
            self.response.out.write(template.render(path, template_values))
        else:
            self.response.out.write("nothing found for idx %d" % idx)  
        
def main():
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/init', Initialise),
                                          ('/keyword', QKeyword),
                                          ('/kanji', QKanji)],
                                         debug=True)
    run_wsgi_app(application)


if __name__ == '__main__':
    main()
