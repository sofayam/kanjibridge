as yet unclassified
renderContentOn: html

 	
	Kanji tagDict allTags do: [ :theTag |
		
 	 	html text:  theTag. 
		html text: ' '.
		(Kanji tagDict objectsWithTag: theTag) do: [ :kj |
			html text: ((Kanji withIndex: kj) glyph)
		].
		html break.	
							

	].

	html break.
	html anchor 
		callback: [ self call: KanjiAdminView new];
		with: 'admin page'.
	
