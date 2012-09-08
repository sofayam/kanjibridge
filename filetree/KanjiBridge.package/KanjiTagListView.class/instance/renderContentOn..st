as yet unclassified
renderContentOn: html

	html text: 'Tags for all Kanjis'.
	html break.
 	
	Kanji tagDict allTags sorted do: [ :theTag |
		
		

		html anchor callback: [ self call: (KanjiTagDeepView new tag: theTag)];
			with: theTag.
		html text: ' '.
		(Kanji tagDict objectsWithTag: theTag) do: [ :alsoTagged |
			html anchor callback: [ self call: (KanjiView new kanji: (Kanji withIndex: alsoTagged)) ]; 
				with: ((Kanji withIndex: alsoTagged) glyph) 
			].
		html break.	
							

	].

	self footer: html

	
