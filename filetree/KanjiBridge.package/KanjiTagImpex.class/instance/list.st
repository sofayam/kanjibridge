as yet unclassified
list
	<get>
	
	" call this with curl -i http:/localhost:8080/impex "

	| f |
	f := FileStream forceNewFileNamed: (KanjiApp homeDirectory , '/kanjibridge/impex/kanjitagbackup.txt' ).
	f nextPutAll: Kanji tagDict asJson.
	f close.
	
	^'OK'
	

