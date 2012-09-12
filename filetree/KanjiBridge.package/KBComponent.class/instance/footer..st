as yet unclassified
footer: html


	" use by adding 
		self footer: html
	at the bottom of the page"
	
	html break.
	html anchor 
		callback: [ self call: KanjiAdminView new];
		with: 'main page'.