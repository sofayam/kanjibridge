as yet unclassified
withWhatever: str otherwise: k 

	(Word hasKanji: str) ifTrue: 
		[^ Word withKanji: str].
	(Word hasKana: str) ifTrue: 
		[^Word withKana: str].
	(Word hasMeaning: str) ifTrue: 
		[^Word withMeaning: str].
	 ^ k
		 
