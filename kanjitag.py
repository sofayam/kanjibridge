import database


def getTags(part=None):
    c = database.cursor()
    if part:
        c.execute("SELECT DISTINCT name FROM kanjitags where (name LIKE '%s%%')") % part
    else:
        c.execute("SELECT DISTINCT name FROM kanjitags")
    res = c.fetchmany(10)
    res = [tup[0] for tup in res]
    return res
    
def getTagCount():
    c = database.cursor()
    c.execute("SELECT COUNT(DISTINCT name) FROM kanjitags")
    res = c.fetchone()[0]
    return res
    

def getTaggedKanjis():
    c = database.cursor()
    c.execute("SELECT kanjitags.name, kanji.glyph, kanji.id FROM kanji, kanjitags WHERE kanjitags.id = kanji.id")
    rows = c.fetchall()
    kwdict = {}
    for row in rows:
        kwd,glyph,idx = row
        if kwd not in kwdict.keys():
            kwdict[kwd] = []
        kwdict[kwd].append((glyph,idx))
    kwarray = []
    for kwd in sorted(kwdict.keys()):
        kwarray.append([kwd, kwdict[kwd]])
    return kwarray
                          

    
