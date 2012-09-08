as yet unclassified
localCommand: fileName

	| cmd |
	cmd :=  '(cd ' , KanjiApp homeDirectory , '/kanjibridge ; ./' , fileName , ')'.

	Transcript show: (PipeableOSProcess command: cmd) output