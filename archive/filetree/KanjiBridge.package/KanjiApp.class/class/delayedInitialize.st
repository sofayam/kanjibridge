as yet unclassified
delayedInitialize

    " delayed and forked so it can be called from the management interface
	without causing an exception"
	
	[(Delay forMilliseconds: 5000) wait.
	Transcript show: 'about to init..'.
	KanjiApp initialize.
	Transcript show: '..finished init' ] fork