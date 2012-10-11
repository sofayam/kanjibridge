as yet unclassified
style: view 

	| always |
	
	always := '  .closed {text-decoration:line-through} '.

	( KanjiApp userAgent: view is: 'ipad')  | ( KanjiApp userAgent: view is: 'ipod') |  ( KanjiApp userAgent: view is: 'Nexus') 
	
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

	' , always
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

	
	' , always