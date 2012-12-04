import json
import database

txt = open("impex/kanjitagbackup.txt").read()
dict = json.loads(txt)

cursor = database.cursor()

for name in dict.keys():
    for idx in dict[name]:
        command = "INSERT INTO kanjitags VALUES ('%s', '%s')" % (idx, name)
        cursor.execute(command)
