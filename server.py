import web
import json
import database

urls = ('/kanji/(.*)/', 'kanji',

        '/neighbours/(.*)/(.*)/', 'neighbours',

        '/onyomi/(.*)/', 'onyomi',

        '/sugg/(.*)/', 'sugg',
        '/suggform/', 'suggform',
)

render = web.template.render('templates')

app = web.application(urls,globals())

class kanji:
    def GET(self,kidx):
        if not kidx:
            kidx = '1'
        c = database.cursor()
        cmd = 'SELECT * FROM kanji WHERE (id = %s)' % kidx
        print "***", cmd
        c.execute(cmd)
        k = c.fetchone()
        return render.kanji(*k)

class neighbours:
    def GET(self,kidx,wdth):
        start = int(kidx)
        finish = int(kidx) + int(wdth)
        c = database.cursor()
        cmd = 'SELECT * FROM kanji WHERE id >= %d and id <= %d' % (start,finish)
        print "***", cmd
        c.execute(cmd)
        batch = c.fetchall()
        return render.neighbours(batch)

class onyomi:
    def GET(self,yomi):
        c = database.cursor()
        yomi = yomi.encode('utf-8')
        cmd = "SELECT kanji.id, kanji.glyph FROM onyomi, kanji WHERE (onyomi.yomi = '%s' AND kanji.id = onyomi.id)" % yomi
        c.execute(cmd)
        batch = c.fetchall()
        return render.onyomi(yomi,batch)

class suggform:
    def GET(self):
        return render.suggform()

class sugg:
    def GET(self,part):
        c = database.cursor()
        cmd = "SELECT kanji.keyword FROM kanji WHERE (kanji.keyword LIKE '%s%%')" % part
        print cmd
        c.execute(cmd)
        res = c.fetchmany(10)
        res = [tup[0] for tup in res]
        web.header('Content-Type', 'application/json')
        return json.dumps(res)

if __name__ == "__main__":
    app.run()
