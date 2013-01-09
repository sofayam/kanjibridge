as yet unclassified
restore
   

	| json f inp todo |
	ToDo initialize.
	KanjiApp doCritical: [
	 f := FileStream oldFileNamed: ToDo backupFileName.
	 inp := f upToEnd.
	 json := JSJsonParser parse: inp.
	 
	   json do: [ :dict |
		todo := ToDo new.
		todo created: (dict at: #created).
		todo text: (dict at: #text).
		todo open: (dict at: #open).
		AllToDos add: todo.

		]
	].

	
	 ^'OK'
	
	
