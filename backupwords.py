import database

import simplejson as json

dict = []

cursor = database.cursor()
command = "SELECT * FROM words"
cursor.execute(command)

rows = cursor.fetchall()


for row in rows:
    dictent = list(row)
    command = "SELECT name FROM wordtags WHERE (id = %s)" % row[0]
    cursor.execute(command)
    names = cursor.fetchall()

    names = [namerow[0] for namerow in names]
    #dict[row[0]] = dictent + [ names ]
    dict.append(  dictent + [ names ] )

f = open("impex/wordbackup.txt", "w")
s = json.dumps(dict, indent=4, sort_keys=True)
f.write(s)
f.close()


