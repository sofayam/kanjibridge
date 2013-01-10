import database
import re
from jchars import *

cursor = database.cursor()

def processWords(subject,payload):

    #print "********Subject:", subject
    #print "++++++++Payload:", payload
    subject = "@" + subject
    words = payload.split("\n\n")
    #print "done split payload"
    for wrd in words:
        print "new word"
        wspli = wrd.split('\n')
        #print "done split word"
        if len(wspli) == 2:
            #print "about to match jbras"
            jbra = "(.*)%s(.*)%s" % (jobr,jcbr)
            sres = re.search(jbra,wrd,re.U)
            #sres = re.search(jbra,wrd.encode('utf-8'),re.U)
            #print "finished match jbras"
            if sres:
                sgro = sres.groups()
                #print "just right : %s < %s >" % sres.groups()

                stashword(kanji=sgro[0],kana=sgro[1],eng=wspli[1],tags=subject)
            
            else:
                for wd in wspli:
                    print "too long : ", wd
            #print "------"
        #f = open("stash.tmp","w")
        #f.write(wd)
        #f.close()



def stashword(kanji,kana,eng,tags,timestamp=None):
    eng = eng.replace("'","")
    #print (kanji, kana, eng, timestamp)
    #print "STASHIT!!! k: %s k: %s e: %s" % (kanji,kana,eng)
    #print kanji,kana
    # check that word is not already there
    command = ("SELECT id FROM words WHERE " +
               "(kanji = '%s' AND kana = '%s' " + 
               "AND english = '%s')") % (kanji, kana, eng)
    if cursor.execute(command) > 0:
        lastid = cursor.fetchone()[0]
        print "*** word entry already exists"
    else:
        if timestamp:
            command = ("INSERT INTO words (kanji, kana, english, created) " + 
                       "VALUES ('%s','%s','%s', '%s')") % (kanji,kana,eng,timestamp)
        else:
            command = ("INSERT INTO words (kanji, kana, english) " + 
                       "VALUES ('%s','%s','%s')") % (kanji,kana,eng)
            
        print "+++ ", command
        cursor.execute(command)
        #print "*** word entry created"
        command = "SELECT LAST_INSERT_ID()"
        cursor.execute(command)
        lastid = cursor.fetchone()[0]
    # check that tag is not already there

    if type(tags) != type([]):      # hack to deal with non dated tags arriving via mail
        tags = [ (tags, None) ]

    for tag, created in tags:
        command = "SELECT * FROM wordtags WHERE (id = %s AND name = '%s')" % (lastid, tag)
        if cursor.execute(command) == 0:
            print "*** inserting word tag"
            if created: 
                command = "INSERT INTO wordtags (id, name, created) VALUES (%d, '%s', '%s')" % (lastid, tag, created)
            else:
                command = "INSERT INTO wordtags (id, name) VALUES (%d, '%s')" % (lastid, tag)
            cursor.execute(command)
        else:
            print "*** tag already exists"


def count():
    cursor.execute("SELECT COUNT(*) FROM words")
    return cursor.fetchone()[0]
