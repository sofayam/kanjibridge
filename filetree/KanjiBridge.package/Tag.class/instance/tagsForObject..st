as yet unclassified
tagsForObject: anObject
	(tagsForObject  includesKey: anObject) ifFalse: [ ^ Set new ].
	^ tagsForObject at: anObject
