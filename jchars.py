# -*- coding: utf-8 -*-
jobr = '（' 

jcbr = '）'

jcomma = '、'


def isKanji(char):
    return (ord(char) >= 0x4E00) and (ord(char) <= 0x9FBF)
