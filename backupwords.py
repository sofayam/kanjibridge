import database

import simplejson as json

dict = []

cursor = database.cursor()
command = "SELECT * FROM words"
cursor.execute(command)

rows = cursor.fetchall()


for row in rows:
    dictent = list(row)
    # print dictent[-1] 
    dictent[-1] = str(dictent[-1]) # cure for datetime/json wierdness
    command = "SELECT name FROM wordtags WHERE (id = %s)" % row[0]
    cursor.execute(command)
    names = cursor.fetchall()

    names = [namerow[0] for namerow in names]
    #dict[row[0]] = dictent + [ names ]
    dict.append(  dictent[:-1] + [ names ] + [ dictent[-1] ] )

#print dict
f = open("impex/wordbackup.txt", "w")
s = json.dumps(dict, indent=4, sort_keys=True)
#print s
f.write(s)
f.close()


