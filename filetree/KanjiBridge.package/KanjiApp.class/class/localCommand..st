as yet unclassified
localCommand: fileName

	| cmd |
	cmd :=  '(cd ' , KanjiApp homeDirectory , '/kanjibridge ; ./' , fileName , ')'.

	PipeableOSProcess command: cmd.