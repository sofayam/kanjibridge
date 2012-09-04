as yet unclassified
isDeployed

	^ FileDirectory default fileExists: ((KanjiApp homeDirectory) , '/kanjibridge/__deployed__' )
	