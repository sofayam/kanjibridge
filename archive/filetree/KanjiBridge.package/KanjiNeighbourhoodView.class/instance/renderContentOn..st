as yet unclassified
renderContentOn: html

	| k |

	html text: 'Neighbourhood'.
	html break.
	html div class: 'kanji'; with: [
	(start to: finish) do: [:id |

		html anchor 
			callback: [ self call: (KanjiView new kanji: (Kanji withIndex: id))];
			with: (Kanji withIndex: id) glyph.
		
		].
	].
	
	self footer: html.