setup
nextKanji: offset

	(self kanji: 
		(Kanji withIndex: 
			(((self kanji) index) asNumber + offset)))
	
