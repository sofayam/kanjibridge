as yet unclassified
renderContentOn: html


	html anchor 
		callback: [ self call: KanjiView new];
		with: 'kanjis'.
		
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
		with: 'backup'.
		
	html break.
	
	html anchor 
		callback: [ self call: KanjiView new];
		with: 'go to application'.
		
	html break.


	html anchor 
		callback: [ KanjiApp delayedInitialize];
		with: 'initialize (Zaps everything)'.
		
	html break.


	
	html text: 'User Agent' , (self session currentRequest headerAt: 'user-agent').
	html break.
	
	
		
	