as yet unclassified
renderContentOn: html

	html form multipart; with: [
			html fileUpload
				callback: [ :value | self receiveFile: value].
			html submitButton: 'Send File']