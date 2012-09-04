as yet unclassified
restore

	| f inp json wrd newWord |
	
	KanjiApp doCritical: [
 	 f := FileStream oldFileNamed: Word backupFileName.
	 inp := f upToEnd.
	 json := JSJsonParser parse: inp.
	 json keysDo: [ : key | 
		wrd := json at: key.
		newWord := Word withKanji: (wrd at: 'kanji') andKana: (wrd at: 'kana') andMeaning: (wrd at: 'meaning').
	      (wrd at: 'tags') do: [:tag | newWord tag: tag]
	 ].
	]
	
