import json
import MySQLdb

txt = open("impex/kanjitagbackup.txt").read()
dict = json.loads(txt)

conn = MySQLdb.connect (host="localhost", user="root", 
                        passwd="blabla", db="kanjibridge")

cursor = conn.cursor()

for name in dict.keys():
    for idx in dict[name]:
        command = "INSERT INTO kanjitags VALUES ('%s', '%s')" % (idx, name)
        cursor.execute(command)
