import web
import string
import json
import re
from jchars import *
import email
import MySQLdb

import smtpd
import asyncore

conn = MySQLdb.connect (host="localhost", user="root", 
                        passwd="blabla", db="kanjibridge")

cursor = conn.cursor()


def stashword(kanji,kana,eng,tag):
    eng = eng.replace("'","")
    #print "STASHIT!!! k: %s k: %s e: %s" % (kanji,kana,eng)
    #print kanji,kana,eng
    command = "INSERT INTO words (kanji, kana, english) VALUES ('%s','%s','%s')" % (kanji,kana,eng)
    #print "Command is >>>", command, "<<<"
    cursor.execute(command)

def processWords(subject,payload):

    #print "********Subject:", subject, "Payload exists"

    words = payload.split("\n\n")
    #print "done split payload"
    for wrd in words:
        #print "new word"
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
                stashword(kanji=sgro[0],kana=sgro[1],eng=wspli[1],tag=subject)
            
            else:
                for wd in wspli:
                    print "too long : ", wd
            print "------"
        #f = open("stash.tmp","w")
        #f.write(wd)
        #f.close()

class CustomSMTPServer(smtpd.SMTPServer):
    
    def process_message(self, peer, mailfrom, rcpttos, data):
        #print 'Receiving message from:', peer
        #print 'Message addressed from:', mailfrom
        #print 'Message addressed to  :', rcpttos
        #print 'Message length        :', len(data)
        msg = email.message_from_string(data)
        subject = msg.get('Subject')
        payload = msg.get_payload()
        processWords(subject,payload)
        return

server = CustomSMTPServer(('0.0.0.0', 25), None)

asyncore.loop()


