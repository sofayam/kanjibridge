lookup
containsString:   str

	  
	 | filtered |
	filtered := Kanji allKeywords 
		select: [ :each | each includesSubstring: str caseSensitive: false ].
	filtered size > 10
		ifTrue: [ filtered := filtered first: 10 ].
	^ filtered 
	
