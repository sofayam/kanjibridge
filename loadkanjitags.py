import json
import database

txt = open("impex/kanjitagbackup.txt").read()
dict = json.loads(txt)

cursor = database.cursor()

for name in dict.keys():
    for idx,created in dict[name]:
        command = "INSERT INTO kanjitags VALUES ('%s', '%s', '%s')" % (idx, name, created)
        cursor.execute(command)
