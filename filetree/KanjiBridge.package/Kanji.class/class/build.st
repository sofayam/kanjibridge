setup
build
	
	| kw mn k kun |
	

	kw :=  Kanji grabfile: 'keywords'.
	kw do: [ :line |
		Kanji newWithGlyph: (line at: 1) 
			andKeyword: ((line at: 2) copyReplaceAll: ' ' with: '_') 
			andIndex: (line at:  4)
	].
	mn := Kanji grabfile: 'meanings'.
	mn do: [ :line |
		k := Kanji withIndex: (line at: 3).
		((line size) < 5)  ifTrue: [ kun := '' ] ifFalse: [kun := (line at: 5)].   
		k setMeaning: (line at: 2) andOn: (line at: 4) andKun: kun  	
	]