as yet unclassified
renderContentOn: html

     html form: [
	html text: 'Add ToDo '.
	html textInput
		id: 'f';
		size: 40 ;
		callback: [ :txt | KanjiApp doCriticalDirty: [ToDo withText: txt ]].
	].

      html break.
	html text: 'List  of of all ToDos.'.
	html break.
	html table:
		[ToDo AllToDos do: [ :todo |
			html tableRow: [
				
		  		html tableData: todo created.
				
				html tableData: [html div class: (todo openAsString); with: (todo text)].
				
				html tableData: [
		  			html anchor 
					 	callback: [ todo toggle ];
						with: (todo openAsString)
				]
			]

		]
	].
	html break.
	self footer: html.

 