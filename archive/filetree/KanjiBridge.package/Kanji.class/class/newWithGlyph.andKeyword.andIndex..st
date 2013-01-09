init
newWithGlyph: aGlyph andKeyword: aKeyword andIndex: anIndex
	"comment stating purpose of message"

	| newObj  |
	
	newObj := Kanji new.
	newObj glyph: aGlyph.
	newObj keyword: aKeyword.
	newObj index: anIndex.
	Kanji addToDicts: newObj.
	
	^ newObj