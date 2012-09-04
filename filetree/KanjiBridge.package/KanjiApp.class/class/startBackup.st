as yet unclassified
startBackup
	bgbackup := true.
	[[bgbackup] whileTrue: [
		Transcript show: ('attempting at ', Time now asString). 
		KanjiApp backupIfDirty.
		(Delay forMilliseconds: 5000) wait ] ]
	fork