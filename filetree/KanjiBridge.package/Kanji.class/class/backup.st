as yet unclassified
backup

	
	| f |
	KanjiApp doCriticalClean: [
	  f := FileStream forceNewFileNamed: (KanjiApp homeDirectory , '/kanjibridge/impex/kanjitagbackup.txt' ).
	  f nextPutAll: Kanji tagDict asJson.
	  f close.
	]
	
	
