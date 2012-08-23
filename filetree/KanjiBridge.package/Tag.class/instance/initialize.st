as yet unclassified
initialize
	objectsWithTag ifNil: [objectsWithTag := Dictionary new].
	tagsForObject ifNil: [tagsForObject := Dictionary new].
	