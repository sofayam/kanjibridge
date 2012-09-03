as yet unclassified
backup

	| f |
	KanjiApp doCriticalClean: [
	  f := FileStream forceNewFileNamed: (KanjiApp homeDirectory , '/kanjibridge/impex/wordbackup.txt' ).
	  f nextPutAll: Word allWords asJson.
	  f close.
	]
