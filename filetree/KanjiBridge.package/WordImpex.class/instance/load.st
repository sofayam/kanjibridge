as yet unclassified
load
	<post>
	<consumes: '*/json'>
	
	" 	
	load words from Japanese Dictionary app via GAE mail/json gateway
	"
	
	| json body entries subject opb clb opbOff clbOff kana kanji word firstCR jap meaning |
	

     json := JSJsonParser parse: self requestContext request rawBody.

     "Transcript show: json."
	subject := json at: 'subject'.
      body := json at: 'body'.

     opb := Character value: 65288.
     clb := Character value: 65289.

	entries := body.

	KanjiApp doCritical: [
	entries do: [ :entry |
		firstCR := entry findString: (String with: (Character lf)).
		jap := entry copyFrom: 1 to: (firstCR - 1).
		meaning := entry copyFrom: (firstCR + 1) to: (entry size).
		
		opbOff := jap findString: (String with: opb).
		clbOff := jap findString: (String with: clb).
		 (opbOff < clbOff) ifTrue: [ 
		 	kana :=  jap copyFrom: opbOff + 1 to: clbOff -1.
			kanji := jap copyFrom: 1 to: opbOff - 1.
		 	"Transcript show: '<<Entry'.
		  	Transcript show: 'jap ', jap.
		 	Transcript show: 'meaning ' , meaning , '>>'.	"
	        	word := Word withKanji: kanji  andKana: kana andMeaning: meaning.
			word tag: subject.
		]
	   ]
		 
	].
	

	
	 ^'OK'
	