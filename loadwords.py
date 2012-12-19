import json
import word

f = open("impex/wordbackup.txt")
wrds = json.loads(f.read())

for wrd in wrds:
    word.stashword(*wrd[1:])
