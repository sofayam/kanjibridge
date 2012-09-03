as yet unclassified
initialize 

	"pointless comment"
	
	dirty := false.
	kanjiLock := Semaphore forMutualExclusion.
	
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
	
