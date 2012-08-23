as yet unclassified
userAgent: view is:  shortName 


	| fullName |
	
	
	fullName := view session currentRequest headerAt: 'user-agent'.
	
	^fullName includesSubstring: shortName caseSensitive: false.
	

	