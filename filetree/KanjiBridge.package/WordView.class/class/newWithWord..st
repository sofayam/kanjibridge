as yet unclassified
newWithWord: aWord
	| wv |
	wv := WordView new.
	wv word: aWord.
	^wv