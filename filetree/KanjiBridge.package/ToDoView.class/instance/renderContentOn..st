as yet unclassified
renderContentOn: html

     html form: [
	html text: 'Add ToDo '.
	html textInput
		id: 'f';
		size: 40 ;
		callback: [ :txt | ToDo withText: txt ].
	].


	html text: 'List  of of all ToDos.'.
	html break.
	
	ToDo AllToDos do: [ :todo |
		html form: [
		  html text: ((todo created) , ' - ' , (todo text) , ' - ' , (todo open asString)).
		  html select
			list: #(#open #closed);
			selected: todo open;
			beSubmitOnChange;
			callback: [ :value |  todo open: value ].
		html break.
		]
	].
	
	self footer: html.

 