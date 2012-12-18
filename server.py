import web
import json
import database

urls = ('/kanji/(.*)/', 'kanji',

        '/neighbours/(.*)/(.*)/', 'neighbours',

        '/onyomi/(.*)/', 'onyomi',

        '/kwsugg/(.*)/', 'kwsugg',

        '/ktsugg/(.*)/', 'ktsugg',

        '/ktag/(.*)/', 'ktag',

        '/addKanjiTag/(.*)/(.*)/', 'addKanjiTag',

)

render = web.template.render('templates')

app = web.application(urls,globals())

class kanji:
    def GET(self,kidx):
        if not kidx:
            kidx = '1'
        c = database.cursor()
        if kidx.isdigit():
            cmd = 'SELECT * FROM kanji WHERE (id = %s)' % kidx
        else:
            cmd = "SELECT * FROM kanji WHERE (keyword = '%s')" % kidx
        print "***", cmd
        c.execute(cmd)
        k = c.fetchone()
        #print "+++k ", k
        kidx = k[0]
        cmd = 'SELECT name FROM kanjitags WHERE (id = %s)' % kidx
        print "***", cmd

        c.execute(cmd)
        kt = c.fetchall()
        #print "+++kt ", kt
        kt = [tup[0] for tup in kt]
        args = list(k) + [ kt ]
        #print "+++args ", args
        return render.kanji(*args)

class addKanjiTag:
    def GET(self,kidx,tag):
        c = database.cursor()
        cmd = "INSERT INTO kanjitags VALUES (%s, '%s')" % (kidx,tag)
        c.execute(cmd)
        web.redirect('/kanji/%s/' % kidx)
        

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

class ktag:
    def GET(self,name):
        c = database.cursor()
        cmd = "SELECT kanji.id, kanji.glyph, kanji.keyword FROM kanji, kanjitags WHERE kanji.id = kanjitags.id and kanjitags.name = '%s'" % (name)
        print "***", cmd
        c.execute(cmd)
        batch = c.fetchall()
        return render.ktag(name,batch)


class onyomi:
    def GET(self,yomi):
        c = database.cursor()
        yomi = yomi.encode('utf-8')
        cmd = "SELECT kanji.id, kanji.glyph FROM onyomi, kanji WHERE (onyomi.yomi = '%s' AND kanji.id = onyomi.id)" % yomi
        c.execute(cmd)
        batch = c.fetchall()
        return render.onyomi(yomi,batch)


class kwsugg:
    def GET(self,part):
        c = database.cursor()
        cmd = "SELECT kanji.keyword FROM kanji WHERE (kanji.keyword LIKE '%s%%')" % part
        print cmd
        c.execute(cmd)
        res = c.fetchmany(10)
        res = [tup[0] for tup in res]
        web.header('Content-Type', 'application/json')
        return json.dumps(res)

class ktsugg:
    def GET(self,part):
        c = database.cursor()
        cmd = "SELECT DISTINCT name FROM kanjitags WHERE (name LIKE '%s%%')" % part
        print cmd
        c.execute(cmd)
        res = c.fetchmany(10)
        res = [tup[0] for tup in res]
        web.header('Content-Type', 'application/json')
        return json.dumps(res)
        

if __name__ == "__main__":
    app.run()
