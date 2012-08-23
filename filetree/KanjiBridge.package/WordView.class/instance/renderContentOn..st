as yet unclassified
renderContentOn: html

      html form: [
	html text: 'Search '.
	html textInput
		id: 'f';
		size: 15 ;
		autocapitalize: 'off';
		script: (html jQuery this autocomplete
			sourceCallback: [ :term | Word containsString: term]);
		callback: [ :value | self word:  (Word withWhatever: value otherwise: word)].
	].
	
	html break.
	html div
		class: 'kanji';
		with: self word kanji.
	html break.
      html text: (self word kana).
	html break.
      html text: (self word meaning).

	html break.
	
	(self word usedKanji) do: [ :kanji |
		html anchor
			callback: [ self call: (KanjiView new kanji: kanji) ];
			with: ((kanji glyph) , ' ' , (kanji keyword)).
		      html break.
	].

	html break.
	html break.
	html text: 'TAGS'.
	html break.
	
	(Word tagsForObject:  (self word)) do: [ :name |
		html text: name.
		(Word objectsWithTag: name) do: [ :alsoTagged |
			html anchor callback: [ word := alsoTagged ]; 
				with: ((alsoTagged kanji) , ' ')
			].
		html anchor callback: [ word deleteTag: name]; with: 'del'.
		html break. 
	].
      html form: [
		html text: 'New Tag '.
		html textInput
			id: 't';
			autocapitalize: 'off';
			size: 15;
			script: (html jQuery this autocomplete
				sourceCallback: [ :term | Word containsTag: term]);
			callback: [ :value | (self word) tag: value].
	].	

		