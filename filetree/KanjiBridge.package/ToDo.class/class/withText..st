as yet unclassified
withText: txt
	| todo |
	
	AllToDos ifNil: [ AllToDos := LinkedList new].
	
	todo := ToDo new.
	todo text: txt.
	todo created: Date today ddmmyyyy.
	todo open: true.
	AllToDos add: todo.
	
	^ todo