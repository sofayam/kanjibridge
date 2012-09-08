tagging
containsTag:   str

	  
	 | filtered |
	filtered := (Kanji tagDict allTags) 
		select: [ :each | each includesSubstring: str caseSensitive: false ].
	filtered size > 10
		ifTrue: [ filtered := filtered first: 10 ].
	^ filtered 
	
