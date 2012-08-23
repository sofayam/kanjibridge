as yet unclassified
objectsWithTag: aName
	(objectsWithTag includesKey: aName) ifFalse: [ ^ Set new ].
	^ objectsWithTag at: aName