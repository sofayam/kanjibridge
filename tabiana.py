import codecs
import mergeinput

dict = {}

def adddict(u):
    if u not in dict.keys():
        dict[u] = 0
    dict[u] += 1


txt = codecs.open("tabi.txt",encoding='sjis_2004').read()

for u in txt:
    adddict(u)

#for k in sorted(dict.keys()):
#    print ord(k), ':', dict[k], ':', k


m = mergeinput.merge()

hdict = {}

for k in m.keys():
    hdict[m[k]['glyph'].decode('utf-8')] = k

for k in sorted(dict.keys()):
    obscure = "*** obscure"
    if k not in hdict.keys():
        res = "*** very obscure"
    else:
        res = m[hdict[k]]['keyword']
        if hdict[k] < 2020: 
            obscure = ""
    print dict[k],k,res,obscure
    
