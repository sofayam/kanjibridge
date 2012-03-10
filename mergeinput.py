import meanings
import keywords


class KanjiX:
    def __init__(self, idx, keyword, glyph):
        self.idx = int(idx)
        self.keyword = keyword
        self.glyph = glyph
        self.meaning = ""
        self.on = ""
        self.kun = ""

    def expl(self):
        print "ID: %s, keyword: %s, glyph: %s" % (self.idx, self.keyword, self.glyph)

def force_utf8(s):
    if type(s) == str:
        return s
    return s.encode('utf-8')

def merge():
    kd = {}
    for keyword in keywords.keywords:
        fields = keyword.split("\t")
        k = {'idx': int(fields[4]), 'keyword': fields[1], 'glyph': force_utf8(fields[0])}
        kd[k['idx']] = k


    for meaning in meanings.meanings:
        fields = meaning.split("\t")
        idx = int(fields[3])
        kd[idx]['meaning'] = fields[1]
        kd[idx]['on'] = force_utf8(fields[4])
        kd[idx]['kun'] = force_utf8(fields[5])

    return kd



    
