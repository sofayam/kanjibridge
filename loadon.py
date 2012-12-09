import mergeinput
import jchars
import database

dict = mergeinput.merge()

ondict = {}

cursor = database.cursor()

for id in dict.keys():
    ons = dict[id]['on']
    #print ons
    for onyomi in ons.split(jchars.jcomma):
        if onyomi not in ondict.keys():
            ondict[onyomi] = []
        ondict[onyomi].append(id)

for onyomi in sorted(ondict.keys()):
    print onyomi, ondict[onyomi]
    for id in ondict[onyomi]:
        cmd = "INSERT INTO onyomi VALUES('%s', %s)" % (onyomi, id)
        cursor.execute(cmd)

print len(ondict.keys())

