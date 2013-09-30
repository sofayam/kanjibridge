import codecs
import jchars
import re

n3dict={}
n45dict={}
commonest={}

n3 = codecs.open("N3.txt",encoding="utf-8").read()
n45 = codecs.open("N45.txt",encoding="utf-8").read()
freq = codecs.open("freq.txt",encoding="utf-8").readlines()
rtk = codecs.open("keywords.txt",encoding="utf-8").readlines()

# make rtk dicts btw kanji and id (1 or 3?)
id2k={}
k2id={}
rtk1=2042
rtk13=3007
for i in range(0,rtk1):
    kid = i + 1
    k = rtk[i][0]
    id2k[kid]=k
    k2id[k]=kid




# make a dictionary for which is the most common word containing kanji k

for idx,l in enumerate(freq):
    wd = re.split("\t",l)[1]
    for k in wd:
        if k not in commonest:
            commonest[k]=(wd,idx)

#print len(commonest)
#for k in commonest.keys()[0:30]:
#    print k, commonest[k]

for k in n3:
    if jchars.isKanji(k):
        n3dict[k]=1

for k in n45:
    if jchars.isKanji(k):
        n45dict[k]=1

anki=n45dict.keys()

#-----------------------------
# RTK1 Kanji not in current deck(s)

notin45 = 0
notin3 = 0
notineither = 0
holdouts = {}

for k in k2id:
    not3 = False
    not45 = False
    if k not in n45dict:
        not45 = True
        notin45 += 1
    if k not in n3dict:
        not3 = True
        notin3 += 1
    if not3 and not45:
        notineither += 1
        holdouts[k]=True    


for h in holdouts:
    if h in commonest:
        print h, ":", (commonest[h][0]).rstrip(), ":", commonest[h][1]
    else:
        print h, "*RARITY*"



print "not in 45", notin45
print "not in 3", notin3
print "not in either", notineither

