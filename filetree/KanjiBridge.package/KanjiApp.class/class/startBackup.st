as yet unclassified
startBackup
	bgbackup := true.
	[[bgbackup] whileTrue: [
		Transcript show: ('backing up at ', Time now asString). 
		(Delay forMilliseconds: 1000) wait ] ]
	fork