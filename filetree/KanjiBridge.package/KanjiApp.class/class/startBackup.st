as yet unclassified
startBackup

	KanjiApp bgbackup ifTrue: [ 
		Transcript show: 'backup (probably) already running, use stopBackup first'.
	]  ifFalse: [
	KanjiApp bgbackup: true.
	[[KanjiApp bgbackup] whileTrue: [
		Transcript show: '.' . "('attempting at ', Time now asString)." 
		KanjiApp backupIfDirty.
		(Delay forMilliseconds: 5000) wait ] ]
	fork
	]