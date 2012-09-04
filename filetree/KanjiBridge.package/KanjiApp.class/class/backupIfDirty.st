as yet unclassified
backupIfDirty

	(KanjiApp isDirty) ifTrue:
	   [	
			KanjiApp backup.
			Transcript show: '*backed up*'
	 ]