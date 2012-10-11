as yet unclassified
localCommand: fileName

	| cmd resTxt |
	cmd :=  '(cd ' , KanjiApp homeDirectory , '/kanjibridge ; ./' , fileName , ')'.

	resTxt := (PipeableOSProcess command: cmd) output.
	
	Transcript show: resTxt.
	
	^ resTxt