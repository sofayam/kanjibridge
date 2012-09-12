as yet unclassified
backup

	
	| f |
	KanjiApp doCriticalClean: [
	  f := FileStream forceNewFileNamed: ToDo backupFileName.
	  f nextPutAll: ToDo AllToDos asJson.
	  f close.
	]
	
	
