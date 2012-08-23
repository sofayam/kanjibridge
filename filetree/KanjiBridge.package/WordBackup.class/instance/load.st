as yet unclassified
load
	<post>
	<consumes: '*/json'>
	
	" 	
	load words from backup
	"
	| json wrd inp |
	
	inp := self requestContext request rawBody base64Decoded.

     json := JSJsonParser parse:  inp.

	json keysDo: [ :key | 
		wrd := json at: key.
		Word withKanji: (wrd at: 'kanji') andKana: (wrd at: 'kana') andMeaning: (wrd at: 'meaning').
	]

