from google.appengine.ext import db

class Kanji(db.Model):
    idx = db.IntegerProperty()
    keyword = db.StringProperty()
    glyph = db.StringProperty()
    meaning = db.StringProperty()
    on = db.StringProperty()
    kun = db.StringProperty()

