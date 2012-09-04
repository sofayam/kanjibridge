as yet unclassified
renderContentOn: html


	html anchor 
		callback: [ self call: KanjiView new];
		with: 'go to application'.
		
	html break.

	html anchor 
		callback: [ self call: KanjiTagListView new];
		with: 'ktags'.
		
	html break.
	



	html text: '------------ Admin Stuff --------'.
	html break.
	
	
	
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

	html anchor 
		callback: [ KanjiApp stopBackup ];
		with: 'stop background backup'.
		
	html break.



	html anchor 
		callback: [ KanjiApp delayedInitialize];
		with: 'initialize (Zaps everything)'.
		
	html break.


	
	html text: 'User Agent' , (self session currentRequest headerAt: 'user-agent').
	html break.
	
	
		
	