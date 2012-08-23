as yet unclassified
withKanji: aKanji andKana: aKana andMeaning: aMeaning
	| word |
	(allWords includesKey: aKanji) ifTrue: [^ false].
	
	KanjiApp setDirty.
	word := Word new.
	word usedKanjiInit.
	word kanji: aKanji.
	word kana: aKana.
	word meaning: aMeaning.
	word addToKanjiDict.
	allWords at: aKanji put: word.
	allWordsByKana at: aKana put: word.
	allWordsByMeaning at: aMeaning put: word.
	^ word
	