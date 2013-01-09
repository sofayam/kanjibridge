import wordutils
import sys

fn = sys.argv[1]

f = open(fn + ".txt").read()

f = f.replace('\r','')

wordutils.processWords(fn,f)
