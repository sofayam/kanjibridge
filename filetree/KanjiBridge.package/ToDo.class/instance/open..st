as yet unclassified
open: status
	(status = 'true') ifTrue: [^open := true].

	(status = 'false') ifTrue: [^open := false].
	
	open := status