import database

cursor = database.cursor()

def stashword(kanji,kana,eng,tag):
    eng = eng.replace("'","")
    #print "STASHIT!!! k: %s k: %s e: %s" % (kanji,kana,eng)
    #print kanji,kana
    command = "INSERT INTO words (kanji, kana, english) VALUES ('%s','%s','%s')" % (kanji,kana,eng)
    #print "Command is >>>", command, "<<<"
    cursor.execute(command)
