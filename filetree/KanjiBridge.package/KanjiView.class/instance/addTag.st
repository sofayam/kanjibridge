display
addTag
	| name |
	KanjiApp doCriticalDirty: [
		
		name := self request: 'Tag name'.
		(self kanji) tag: name
		
	]
	"Tag named: name onObject: (self kanji)."
	
	