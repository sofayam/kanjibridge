import web
import string
import json
import re
from jchars import *

urls = ('/(.*)', 'store')

app = web.application(urls,globals())

def stashword(kanji,kana,eng):
    #print "k: %s k: %s e: %s" % (kanji,kana,eng)
    print kanji,kana,eng


class store:
    def GET(self,name):
        if not name:
            name = 'World'
        return 'Hello ' + name + '!'

    def POST(self,name):
        if not name:
            name = 'World'
        wi = web.input()
        wd = web.data()
        #print wi
        #print wd
        jwd = json.loads(wd)
        tag = jwd['subject']
        body = jwd['body']
        for wrd in body:
            wspli = wrd.split('\n')
            if len(wspli) == 2:

                jbra = "(.*)%s(.*)%s" % (jobr,jcbr)
                sres = re.search(jbra,wrd.encode('utf-8'),re.U)

                if sres:
                    sgro = sres.groups()
                    print "just right : %s < %s >" % sres.groups()
                    stashword(kanji=sgro[0],kana=sgro[1],eng=wspli[1])
            
            else:
                for wd in wspli:
                    print "too long : ", wd
            print "------"
        #f = open("stash.tmp","w")
        #f.write(wd)
        #f.close()
        return 'Hello ' + string.join(web.input().keys()) + '!'



if __name__ == "__main__":
    app.run()
