as yet unclassified
dependencies

Gofer new
	squeaksource: 'MetacelloRepository';
	package: 'ConfigurationOfOSProcess';
	load.
	
 (Smalltalk at: #ConfigurationOfOSProcess)  load.

Gofer new
      url: 'http://ss3.gemstone.com/ss/FileTree';
      package: 'ConfigurationOfFileTree';
      load.
    ((Smalltalk at: #ConfigurationOfFileTree) project version: '1.0') load.  

Gofer new
        repository: (MCFileTreeRepository new directory: 
                    (FileDirectory on: '/home/mark/filetree/repository/'));
        package: 'MonticelloFileTree-Core';
        load.


Gofer it
 squeaksource: 'MetacelloRepository';
 package: 'ConfigurationOfRFB';
 load.
((Smalltalk at: #ConfigurationOfRFB) project perform: #latestVersion) load.