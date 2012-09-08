access
kanji: aKanji
	| wordEntries words |

	kanji := aKanji.
	"Now set up children"
	words :=  Word wordsForKanji:  (self kanji index).
	words ifNil: 
		[ self wordChildren: #() ]
	 ifNotNil: 
		[ self wordChildren: (words collect: [ :word | WordEntryView newWithWord: word ] ) ]
	

	
	