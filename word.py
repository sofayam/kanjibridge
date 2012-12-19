import database

cursor = database.cursor()

def stashword(kanji,kana,eng,tags):
    eng = eng.replace("'","")
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
        command = ("INSERT INTO words (kanji, kana, english) " + 
                   "VALUES ('%s','%s','%s')") % (kanji,kana,eng)
        cursor.execute(command)
        print "*** word entry created"
        command = "SELECT LAST_INSERT_ID()"
        cursor.execute(command)
        lastid = cursor.fetchone()[0]
    # check that tag is not already there

    if type(tags) != type([]):
        tags = [ tags ]

    for tag in tags:
        command = "SELECT * FROM wordtags WHERE (id = %s AND name = '%s')" % (lastid, tag)
        if cursor.execute(command) == 0:
            print "*** inserting word tag"
            command = "INSERT INTO wordtags VALUES (%d, '%s')" % (lastid, tag)
            cursor.execute(command)
        else:
            print "*** tag already exists"


