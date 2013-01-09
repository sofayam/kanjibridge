import json
import wordutils

f = open("impex/wordbackup.txt")
wrds = json.loads(f.read())

for wrd in wrds:
    idx,kanji,kana,eng,tags,timestamp = wrd
    kanji = kanji.encode('utf-8')
    kana = kana.encode('utf-8')
    eng = eng.encode('utf-8') 
    timestamp = timestamp.encode('utf-8') 
    wordutils.stashword(kanji,kana,eng,tags,timestamp)
