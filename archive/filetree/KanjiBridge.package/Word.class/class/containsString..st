as yet unclassified
containsString:   str

	  
	 | filtered |
	filtered := ((allWords keys) , (allWordsByKana keys) , (allWordsByMeaning keys))
		select: [ :each | each includesSubstring: str caseSensitive: false ].
	filtered size > 10
		ifTrue: [ filtered := filtered first: 10 ].
	^ filtered 
	
