as yet unclassified
style: view 

	( KanjiApp userAgent: view is: 'ipad')  | ( KanjiApp userAgent: view is: 'ipod') 
	
	ifTrue:
	
	[ ^ '
	body { font-size: 40pt; }
	.text { font-size: 40pt; }
	.kanji { font-size: 100pt;  text-align: center;}
	input[type=text] {
	    height: 50px;
	   /* width: 200px; */


	}
	.ui-autocomplete.ui-menu
	{
	     opacity: 0.4;
 	    list-style-type: none;
  	   	filter: alpha(opacity=40); /* for mozilla */
	}

	'
	].

	" Default style sheet "

	^ '
	
	.kanji { font-size: 20pt;  }
	.ui-autocomplete.ui-menu
	{
	     opacity: 0.4;
 	    list-style-type: none;
  	   	filter: alpha(opacity=40); /* for mozilla */
	}

	
	'