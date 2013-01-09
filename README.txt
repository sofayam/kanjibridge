server.py	-- the HTTP server this is all about
mailman.py 	-- handles incoming mail with wordlists from IOS

mergeinput.py 	-- provides kanjis from massaged csv files
keywords.py	-- raw kanji data
meanings.py	-- more raw kanji data

loadkanjis.py 	-- loads kanjis using mergeinput
loadkanjitags.py -- loads kanji tags from json
loadwords.py	 -- loads words and word tags from json

stashwords.py 	 -- sneaky side entry for testing mail word input

backupwords.py	 -- dumps words and their tags to json
backupkanjitags.py -- dumps kanji tags to json

wordutils.py	   -- parsing and storage of incoming words
jchars.py	   -- japanese characters for use in regexes
kanjitag.py	   -- queries between kanjis and their tags

loadon.py	   -- loads the individual onyomi using mergeinput

