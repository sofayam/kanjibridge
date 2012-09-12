display
renderContentOn: html

     | wordList |
      html form: [
	html text: 'Search '.
	html textInput
		id: 'f';
		size: 15 ;
		autocapitalize: 'off';
		autocorrect: 'off';
		script: (html jQuery this autocomplete
			sourceCallback: [ :term | Kanji containsString: term]);
		callback: [ :value | self kanji:  (Kanji withWhatever: value otherwise: kanji)].
	].
	
	html break.
      html text: (self kanji keyword) , ':',  (self kanji index).
	html div
		class: 'kanji';
		with: self kanji glyph.

	html break.
	
	html anchor 
		callback: [self front. self  nextKanji: -1];
		with:  'Prev'.
	html text: '<--->'.
	html anchor 
		callback: [self front. self  nextKanji: 1];
		with:  'Next'.
	html break.
	
	html break.
	html text: self kanji on, ' // ', self kanji kun.
	html break.
	html text: self kanji meaning.

"	
	self onBack ifFalse: [
		html anchor
			callback: [self back];
			with: 'details'
	] ifTrue: [

		html break.
		html text: self kanji on, ' // ', self kanji kun.
		html break.
		html text: self kanji meaning.
	].
"

	html break.
	html break.
	html text: 'TAGS'.
	html break.
	
	(Kanji tagsForObject:  (self kanji)) do: [ :name |

		html anchor callback: [ self call: (KanjiTagDeepView new tag: name)];
			with: name , ' '.
		(Kanji objectsWithTag: name) do: [ :alsoTagged |
			html anchor callback: [ kanji := alsoTagged ]; 
				with: (alsoTagged glyph) 
			].
		html anchor callback: [ 
			(self confirm: 'Are you sure?')
				ifTrue: [ kanji deleteTag: name]]; 
		with: 'del'.
		html break.
	].
	
	html break.
	

	(wordChildren size = 0)  
		ifTrue: [
		html text: 'No words found for this Kanji'.
		]
		 ifFalse: [ 
			html text: 'Words with this Kanji:'.
			html break.
			wordChildren do: [ :wchild |
				html anchor callback: [ self call: (WordView newWithWord: wchild word)]; with: '#'.
				html render: wchild.
				html break.
			].
		].
		html break.
	

	html form: [
		html text: 'New Tag '.
		html textInput
			id: 't';
			autocapitalize: 'off';
			autocorrect: 'off';
			size: 15;
			script: (html jQuery this autocomplete
				sourceCallback: [ :term | Kanji containsTag: term]);
			callback: [ :value | KanjiApp doCriticalDirty: [ (self kanji) tag: value]].
	].	
	
	self footer: html
	

		