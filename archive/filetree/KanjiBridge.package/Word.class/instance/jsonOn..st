as yet unclassified
jsonOn: aStream

	| dict |
	dict := Dictionary new.
	dict at: 'kana' put: kana; at: 'kanji' put: kanji; at: 'meaning' put: meaning.
	dict at: 'tags' put: self tags.
	aStream nextPutAll: (dict asJson).