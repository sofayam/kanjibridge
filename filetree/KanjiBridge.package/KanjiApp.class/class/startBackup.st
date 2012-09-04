as yet unclassified
startBackup

	bgbackup ifTrue: [ 
		Transcript show: 'backup (probably) already running, use stopBackup first'.
	]  ifFalse: [
	bgbackup := true.
	[[bgbackup] whileTrue: [
		Transcript show: '.' . "('attempting at ', Time now asString)." 
		KanjiApp backupIfDirty.
		(Delay forMilliseconds: 5000) wait ] ]
	fork
	]