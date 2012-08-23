as yet unclassified
load
	<post>
	<consumes: '*/json'>
	
	" 
	 now create a tag dictionary for the kanjis using decoded json 
	curl -H Content-Type: text/json -d @dl.txt http://localhost:8080/impex
	"
	
	| json |
     json := JSJsonParser parse: self requestContext request rawBody.

	
	   json keys do: [ :name |
		(json at: name) do: [ :kId |
			   (Kanji withIndex: kId) tag: name.
			   Transcript show: name, kId asString
			 ] 
		].
	
	Transcript show: json.
	
	 ^'OK'
	
	
