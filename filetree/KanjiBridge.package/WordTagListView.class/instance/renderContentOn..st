as yet unclassified
renderContentOn: html


	html text: 'Tags for all Words'.
	html break. 	

	Word tagDict allTags sorted do: [ :theTag |		
 	 	html text:  theTag. 
		html text: ' '.
		(Word tagDict objectsWithTag: theTag) do: [ :alsoTagged |
			html anchor callback: [ self call: (WordView new word:  alsoTagged) ]; 
				with: ((alsoTagged kanji), ' ') 
			].
		html break.	
							
	].

	self footer: html