as yet unclassified
renderContentOn: html

	html text: 'Kanjis for tag' , theTag.
	html break.
 	(Kanji tagDict objectsWithTag: theTag) do: [ :alsoTagged |
		html anchor callback: [ self call: (KanjiView new kanji: (Kanji withIndex: alsoTagged)) ]; 
			with: ((Kanji withIndex: alsoTagged) keyword).

		html break. 
		html div
			class: 'kanji';
			with: (Kanji withIndex: alsoTagged) glyph.

	html break.

	].

	self footer: html