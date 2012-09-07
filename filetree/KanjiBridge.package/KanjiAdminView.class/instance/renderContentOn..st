as yet unclassified
renderContentOn: html


	html anchor 
		callback: [ self call: KanjiView new];
		with: 'kanji'.
		
	html break.

	html anchor 
		callback: [ self call: KanjiTagListView new];
		with: ('ktags(' , (Kanji tagDict allTags size asString) , ')' ).
		
	html break.

	html anchor 
		callback: [ self call: (WordView newWithWord: (Word anyWord))];
		with: ( 'words (' , Word count asString  , ')' ).
		
	html break.

      html horizontalRule.
	html text: '* A d m i n *'.
      html horizontalRule.	
	
	html anchor
		callback: [ KanjiApp restore];
		with: 'restore'.
		
	html break.
	
	html anchor
		callback: [ KanjiApp backup];
		with: 'one time backup'.
		
	html break.
	
	
	html anchor 
		callback: [ KanjiApp startBackup ];
		with: 'start background backup'.
		
	html break.

	html  text: KanjiApp bgbackupStatus.
	html break.
	html  text: 'Last backup: ' , KanjiApp timeSinceBackup.

	html break.

	html anchor 
		callback: [ KanjiApp stopBackup ];
		with: 'stop background backup'.
		
	html break.



	html anchor 
		callback: [ KanjiApp delayedInitialize];
		with: 'initialize (Zaps everything)'.
		
	html break.

	html anchor 
		callback: [ KanjiApp loadChanges ];
		with: 'load code changes from repository'.
		
	html break.


	
	html text: 'User Agent' , (self session currentRequest headerAt: 'user-agent').
	html break.
	
	
		
	