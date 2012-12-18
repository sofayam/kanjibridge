import MySQLdb

import database

import json

dict = {}

cursor = database.cursor()

command = "SELECT * FROM kanjitags"

cursor.execute(command)

rows = cursor.fetchall()

for row in rows:
    idx = row[0]
    name = row[1]
    if name not in dict.keys():
        dict[name] = []
    dict[name].append(idx)

print json.dumps(dict)
    
