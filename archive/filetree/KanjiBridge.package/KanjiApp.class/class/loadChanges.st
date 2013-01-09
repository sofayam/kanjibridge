as yet unclassified
loadChanges

  [(Delay forMilliseconds: 5000) wait.
   
  KanjiApp pullHg.

  Gofer new
        repository: (MCFileTreeRepository new directory: 
                    (FileDirectory on: (KanjiApp homeDirectory) ,
			'/kanjibridge/filetree/'));
        package: 'KanjiBridge';
        load.

    SmalltalkImage current saveSession.
 ] fork 
