as yet unclassified
withText: txt
	| todo |
	
	todo := ToDo new.
	todo text: txt.
	todo created: DateAndTime now.
	todo open: true.
	^ todo