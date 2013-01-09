as yet unclassified
wordsForKanji: idx

	(kanjiDict includesKey: idx) ifFalse: [ ^ nil ].
	^ kanjiDict at: idx