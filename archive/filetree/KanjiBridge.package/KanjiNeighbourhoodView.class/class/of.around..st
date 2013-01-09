as yet unclassified
of: size around: id
	| half start finish res |
	
	half := size / 2.
	
	start := (id - half) max: 1.
	
	finish := (start + size) min: (KanjiApp maxId).
	
	res := self new.
	
	res start: start finish: finish.
	
	^ res
	
	
	

	