as yet unclassified
addToKanjiDict

	| idx k |
	kanji do: [ :kchar | 
		k := String with: kchar.
		(Kanji hasGlyph: k) ifTrue: [
			idx := (Kanji withGlyph: k) index.
			(kanjiDict includesKey: idx) ifFalse:  [ kanjiDict at: idx put: Set new].
			(kanjiDict at: idx) add: self.
			self addUsedKanji: (Kanji withGlyph: k).
		]
	]