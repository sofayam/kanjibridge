as yet unclassified
backup

	| f |
	KanjiApp doCriticalClean: [
	  f := FileStream forceNewFileNamed: Word backupFileName.
	  f nextPutAll: Word allWords asJson.
	  f close.
	]
