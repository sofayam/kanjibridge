as yet unclassified
timeSinceBackup

	lastBackup ifNil: 
      	 [^ 'none performed']
	 ifNotNil: 
		[^ (DateAndTime now - lastBackup) asString ]