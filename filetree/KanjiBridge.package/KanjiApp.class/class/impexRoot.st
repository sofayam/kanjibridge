as yet unclassified
impexRoot

	| prefix |
	
	prefix := 'test'.
	KanjiApp isDeployed ifTrue: [ prefix := ''].
	^(KanjiApp homeDirectory) , '/kanjibridge/impex/' , prefix