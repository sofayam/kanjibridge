as yet unclassified
named: aName onObject: anObject


	
	(objectsWithTag includesKey: aName) ifFalse:  [ objectsWithTag at: aName put: Set new].
	(objectsWithTag at: aName) add: anObject.
	
	(tagsForObject includesKey: anObject) ifFalse:  [ tagsForObject at: anObject put: Set new].
	(tagsForObject at: anObject) add: aName.

	