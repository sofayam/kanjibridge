lookup
withWhatever: str otherwise: k 
	
	(Kanji hasKeyword: str) ifTrue: 
		[^ Kanji withKeyword: str].
	(Kanji hasIndex: str) ifTrue: 
		[^Kanji withIndex: str].
	(Kanji hasGlyph: str) ifTrue: 
		[^Kanji withGlyph: str].
	 ^ k
		 
