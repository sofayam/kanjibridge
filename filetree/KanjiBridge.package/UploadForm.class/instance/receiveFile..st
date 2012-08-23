as yet unclassified
receiveFile: aFile
	
	count := 0.
	self halt.
	
      lines := (Character lf) split: (aFile rawContents).

	lines do: [:line
		| count := count + 1.		
	]