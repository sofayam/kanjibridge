as yet unclassified
named: aName onObject: anObject

	KanjiApp lock critical: [
		
	KanjiApp setDirty.
	
	(objectsWithTag includesKey: aName) ifFalse:  [ objectsWithTag at: aName put: Set new].
	(objectsWithTag at: aName) add: anObject.
	
	(tagsForObject includesKey: anObject) ifFalse:  [ tagsForObject at: anObject put: Set new].
	(tagsForObject at: anObject) add: aName.
	
	]
	