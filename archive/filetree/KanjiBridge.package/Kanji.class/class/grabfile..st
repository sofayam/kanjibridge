setup
grabfile:  fname
" grab a file and return a list of lists"

| text lines entries home | 

home := KanjiApp homeDirectory.

	
text  := (FileStream oldFileNamed: home, '/kanjibridge/', fname, '.txt') upToEnd. 

lines := text findTokens:  (Character lf) .

entries  := OrderedCollection  new.

lines do: [ :line | 
	| items |
	items := line findTokens:   (Character tab).
	(items size) > 1 ifTrue:
	 [ entries add: items].
	].
 ^ entries.