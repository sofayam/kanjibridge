from google.appengine.ext import db

class Kanji(db.Model):
    idx = db.IntegerProperty()
    keyword = db.StringProperty()
    glyph = db.StringProperty()
    meaning = db.StringProperty()
    on = db.StringProperty()
    kun = db.StringProperty()

class Word(db.Model):
    kaki = db.StringProperty()
    yomi = db.StringProperty()
    meaning = db.StringProperty()

