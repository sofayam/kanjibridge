as yet unclassified
initialize 

	"pointless comment"
	
	dirty := false.
	lock := Semaphore forMutualExclusion.
	
	Kanji initialize.
	KanjiView initialize. 
	KanjiTagBackup initialize. 
	KanjiTagRestore initialize. 
	
	Word initialize.
	WordBackup initialize.
	WordRestore initialize.
	WordImpex initialize.
	WordListView initialize.