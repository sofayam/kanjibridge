as yet unclassified
homeDirectory
	| home |
	(FileDirectory  default directoryExists:  '/Users') ifTrue: [
  		home := '/Users/mark'	
		]  ifFalse: [
		(FileDirectory  default directoryExists:  '/home/mark') ifTrue: [
 			home := '/home/mark'
		] ifFalse: [
			home := '/home/ubuntu'
		]
	].
	^home

