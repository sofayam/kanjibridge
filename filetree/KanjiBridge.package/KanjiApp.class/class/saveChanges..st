as yet unclassified
saveChanges: commitMessage

    Gofer new
        repository: (MCFileTreeRepository new directory: 
                    (FileDirectory on: (KanjiApp homeDirectory) ,
			'/kanjibridge/filetree/'));
        package: 'KanjiBridge';
        commit: commitMessage.
	KanjiApp pushHg: commitMessage.