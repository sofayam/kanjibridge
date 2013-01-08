import json
import wordutils

f = open("impex/wordbackup.txt")
wrds = json.loads(f.read())

for wrd in wrds:
    wordutils.stashword(*wrd[1:])
