import MySQLdb

import mergeinput

dict = mergeinput.merge()

conn = MySQLdb.connect (host="localhost", user="root", 
                        passwd="blabla", db="kanjibridge")

cursor = conn.cursor()

for row in dict.keys():
    print row
    dict[row]['meaning'] = dict[row]['meaning'].replace("'","")
    dict[row]['keyword'] = dict[row]['keyword'].replace("'","")
    command = "INSERT INTO kanji VALUES('%(idx)s','%(glyph)s','%(on)s','%(kun)s','%(keyword)s','%(meaning)s')" % dict[row]
    print command
    cursor.execute(command)

