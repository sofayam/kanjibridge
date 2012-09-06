as yet unclassified
renderContentOn: html

	html text: 'Tags for all Kanjis'.
	html break.
 	
	Kanji tagDict allTags sorted do: [ :theTag |
		
		
 	 	html text:  theTag. 
		html text: ' '.
		(Kanji tagDict objectsWithTag: theTag) do: [ :alsoTagged |
			html anchor callback: [ self call: (KanjiView new kanji: (Kanji withIndex: alsoTagged)) ]; 
				with: ((Kanji withIndex: alsoTagged) glyph) 
			].
		html break.	
							

	].

	html break.
	html anchor 
		callback: [ self call: KanjiAdminView new];
		with: 'admin page'.
	
