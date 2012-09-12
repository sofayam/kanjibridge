as yet unclassified
jsonOn: aStream

	| d |
	d := Dictionary new.
	d at: 'text' put: text.
	d at: 'created' put: created.
	d at: 'open' put: open.
	aStream nextPutAll: d asJson.
