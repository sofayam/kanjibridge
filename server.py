import web
import database

urls = ('/kanji/(.*)/', 'kanji',

        '/neighbours/(.*)/(.*)/', 'neighbours')

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

if __name__ == "__main__":
    app.run()
