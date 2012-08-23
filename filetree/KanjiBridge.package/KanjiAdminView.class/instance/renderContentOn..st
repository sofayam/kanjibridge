as yet unclassified
renderContentOn: html

	html text: 'Kanji Admin Page'.
	html break.
	
	html anchor
		callback: [ Kanji restore. Word restore];
		with: 'restore'.
		
	html break.
	
	html anchor
		callback: [ Kanji backup. Word backup];
		with: 'backup'.
		
	html break.
	
	html anchor 
		callback: [ self call: KanjiView new];
		with: 'go to application'.
		
	html break.
	
	html text: 'User Agent' , (self session currentRequest headerAt: 'user-agent').
	html break.
	
	
		
	