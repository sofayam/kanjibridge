as yet unclassified
initialize 
	
	dirty := false.
	kanjiLock := Semaphore forMutualExclusion.
	lastBackup := nil.
	
	Kanji initialize.
	KanjiView initialize. 
	KanjiTagBackup initialize. 
	KanjiTagRestore initialize. 
	KanjiTagListView initialize.
	
	Word initialize.
	WordBackup initialize.
	WordRestore initialize.
	WordImpex initialize.
	WordListView initialize.
	
