#!/usr/bin/env python
#

from google.appengine.ext import webapp

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
        idx = self.request.get('idx')
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
        
def main():
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/init', Initialise)],
                                         debug=True)
    run_wsgi_app(application)


if __name__ == '__main__':
    main()
