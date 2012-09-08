as yet unclassified
bgbackupStatus

	 KanjiApp bgbackup ifTrue:
	   [ ^ 'background backup running']
	ifFalse: 
	   [ ^ 'background backup not running']