tagging
objectsWithTag: t

	| indices |
	indices := (self tagDict) objectsWithTag: t.
	 ^ indices collect: [:o | Kanji withIndex: o]