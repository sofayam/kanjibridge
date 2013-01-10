import web
import json
import database
import kanjitag
import wordutils

urls = (
        '/', 'index',
        '/kanji/(.*)/', 'kanji',
        '/word/(.*)/', 'word',
        '/words/', 'words',
        '/neighbours/(.*)/(.*)/', 'neighbours',
        '/onyomi/(.*)/', 'onyomi',
        '/kwsugg/(.*)/', 'kwsugg',
        '/ktsugg/(.*)/', 'ktsugg',
        '/wtsugg/(.*)/', 'wtsugg',
        '/wsugg/(.*)/', 'wsugg',
        '/ktag/(.*)/', 'ktag',
        '/ktags/', 'ktags',
        '/addKanjiTag/(.*)/(.*)/', 'addKanjiTag',
        '/addWordTag/(.*)/(.*)/', 'addWordTag',

        '/wordsForTag/(.*)/', 'wordsForTag',
        '/style.css', 'style',
)

render = web.template.render('templates')

app = web.application(urls,globals())

class index:
    def GET(self):
        ktagcount = kanjitag.getTagCount()
        wordcount = wordutils.count()
        agent = web.ctx.env['HTTP_USER_AGENT']
        return render.index(ktagcount,wordcount,agent)

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

class word:
    def GET(self,widx):
        if not widx:
            widx = '1'
        c = database.cursor()
        if widx.isdigit():
            cmd = 'SELECT * FROM words WHERE (id = %s)' % widx
        else:
            cmd = "SELECT * FROM words WHERE (kanji = '%s')" % widx
        print "***", cmd
        c.execute(cmd)
        w = c.fetchone()
        #print "+++w ", w
        widx = w[0]
        cmd = 'SELECT name FROM wordtags WHERE (id = %s)' % widx
        print "***", cmd

        c.execute(cmd)
        wt = c.fetchall()
        #print "+++wt ", wt
        wt = [tup[0] for tup in wt]
        args = list(w) + [ wt ]
        print "+++args ", args
        return render.word(*args)

class words:
    def GET(self):
        c = database.cursor()
        # for each source tag
        cmd = 'SELECT DISTINCT name FROM wordtags'
        c.execute(cmd)
        wt = c.fetchall()
        wt = [tup[0] for tup in wt]
        return render.words(wt)

class wordsForTag:
    def GET(self,tag):
        # find all the words with this tag and retrieve the id and kanji
        c = database.cursor()
        cmd = "SELECT words.id, words.kanji FROM words, wordtags WHERE wordtags.name = '%s' AND wordtags.id = words.id" % tag
        c.execute(cmd)
        wfts = c.fetchall()        
        return render.wordsForTag(tag, wfts)

class addKanjiTag:
    def GET(self,kidx,tag):
        c = database.cursor()
        cmd = "INSERT INTO kanjitags (id, name) VALUES (%s, '%s')" % (kidx,tag)
        c.execute(cmd)
        web.redirect('/kanji/%s/' % kidx)

class addWordTag:
    def GET(self,widx,tag):
        c = database.cursor()
        cmd = "INSERT INTO wordtags (id, name) VALUES (%s, '%s')" % (widx,tag)
        c.execute(cmd)
        web.redirect('/word/%s/' % widx)
        

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

class ktags:
    def GET(self):
        taglist = kanjitag.getTaggedKanjis()
        return render.ktags(taglist)

class onyomi:
    def GET(self,yomi):
        c = database.cursor()
        yomi = yomi.encode('utf-8')
        cmd = "SELECT kanji.id, kanji.glyph FROM onyomi, kanji WHERE (onyomi.yomi = '%s' AND kanji.id = onyomi.id)" % yomi
        c.execute(cmd)
        batch = c.fetchall()
        return render.onyomi(yomi,batch)


class style:
    def GET(self):
        mobile = 'mobile' in web.ctx.env['HTTP_USER_AGENT'].lower() 
        #mobile = True
        return render.style(mobile)


#------------------------------- J S O N -------------------------------------

class kwsugg:
    def GET(self,part):
        c = database.cursor()
        #res = kanjitag.getTags(part)  # B U G
        cmd = "SELECT kanji.keyword FROM kanji WHERE (keyword LIKE '%s%%')" % part
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

class wsugg:
    def GET(self,part):
        c = database.cursor()
        cmd = "SELECT DISTINCT kanji FROM words WHERE (kanji LIKE '%s%%')" % part
        print cmd
        c.execute(cmd)
        res = c.fetchmany(10)
        res = [tup[0] for tup in res]
        web.header('Content-Type', 'application/json')
        return json.dumps(res)

        
class wtsugg:
    def GET(self,part):
        c = database.cursor()
        cmd = "SELECT DISTINCT name FROM wordtags WHERE (name LIKE '%s%%')" % part
        print cmd
        c.execute(cmd)
        res = c.fetchmany(10)
        res = [tup[0] for tup in res]
        web.header('Content-Type', 'application/json')
        return json.dumps(res)


if __name__ == "__main__":
    app.run()
