as yet unclassified
backup

	
	| f |
	KanjiApp doCriticalClean: [
	  f := FileStream forceNewFileNamed: Kanji backupFileName.
	  f nextPutAll: Kanji tagDict asJson.
	  f close.
	]
	
	
