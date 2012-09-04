as yet unclassified
bgbackupStatus

	 bgbackup ifTrue:
	   [ ^ 'background backup running']
	ifFalse: 
	   [ ^ 'background backup not running']