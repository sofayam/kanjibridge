import jchars
import codecs
import mergeinput

dict = {}

pops = {}

def adddict(u):
    if not jchars.isKanji(u):
        return 
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
normalctr = 0
obscurectr = 0 
vobscurectr = 0 
for k in m.keys():
    hdict[m[k]['glyph'].decode('utf-8')] = k

for k in sorted(dict.keys()):
    obscure = "*** obscure"
 
    if k not in hdict.keys():
        res = "*** very obscure"
        vobscurectr += 1 
    else:
        res = m[hdict[k]]['keyword']
        if hdict[k] <= 2042:
            normalctr += 1 
            obscure = ""
        else:
            obscurectr += 1
    print dict[k],k,res,obscure

for k in dict.keys():
    count = dict[k]
    if count not in pops.keys():
        pops[count] = []
    pops[count].append(k)

print "%d normal %d obscure %d very obscure" % (normalctr, obscurectr, vobscurectr)

for pop in pops.keys():
    print pop
    for k in pops[pop]: print k,
    print
    
