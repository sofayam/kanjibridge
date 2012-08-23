as yet unclassified
initialize 

  | application |
	application := WAAdmin register: self asApplicationAt: 'kanji'.
	
	application preferenceAt: #scriptGeneratorClass put: JQScriptGenerator.
	
	application
		addLibrary: JQDeploymentLibrary;
		addLibrary: JQUiDeploymentLibrary