as yet unclassified
deleteTag: aName onObject: anObject
	
	(objectsWithTag at: aName) remove: anObject.
	(objectsWithTag at: aName) isEmpty ifTrue:  [objectsWithTag removeKey: aName].
	
	
	(tagsForObject at: anObject) remove: aName.
	(tagsForObject at: anObject) isEmpty ifTrue: [tagsForObject removeKey: anObject].
	