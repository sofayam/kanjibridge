as yet unclassified
restore
   

	| json f inp |
	KanjiApp doCritical: [
	 f := FileStream oldFileNamed: Kanji backupFileName.
	 inp := f upToEnd.
	 json := JSJsonParser parse: inp.
	
	   json keys do: [ :nomen |
		(json at: nomen) do: [ :kId |
			   (Kanji withIndex: kId) tag: nomen.
			  
			 ] 
		]
	].

	
	 ^'OK'
	
	
