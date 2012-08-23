as yet unclassified
renderContentOnOld: html

 	
	Word allWords valuesDo: [ :aword |
	
 	 	html text: (aword kanji). 
		html break.
		html text: (aword kana). 
		html break.
		html text: (aword meaning). 
		html break.
		html break.
].