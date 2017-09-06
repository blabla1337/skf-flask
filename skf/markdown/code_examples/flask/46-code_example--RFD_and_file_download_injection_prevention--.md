# Reflective file download and file download injection prevention
-------

## Example:

    
	def downloadUserFiles(fileId):
		
		proceed = True

		"""
		For the sake of example we only allow the users to download their own files
		by identifier based sql query's. As you can see we select the filename
		by its id. in this case we prevent direct userinput into the disposition header.
		"""

		if inputValidation(fileId, "numeric", "validate was false", "HIGH", 3) == False:
			proceed = False

		if proceed = True:
			file = Download.query.filter_by(fileId=fileId, userId=session['id']).first()

			filename = file.fileName
			mimeType = file.mimeType

			if filename:

				"""
				We also define the mimetype per download file.
				This is because whenever a user can only download images it is not necessary to set
				an uncommon content-type header for it.
				NOTE: These mimetypes should not be stored based upon the mimetype which was send
				the reponse header when the user uploaded the file. This value can be easily
				manipulated with an intercepting proxy. You should get the mimetype from the file
				itself after it was stored on the server.
				"""

				response = Response(open(app.config['UPLOAD_FOLDER'] + filename).read())
				response.headers["Content-Description"] = "File Transfer"
				response.headers["Content-type"] = mimeType
				response.headers["Content-Disposition"] = "attachment; filename=" + filename
				response.headers["Expires"] = 0
				response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
				response.headers["Cache-Control"] = "post-check=0, pre-check=0", false

				if os.path.exists(app.config['UPLOAD_FOLDER'] + filename):
        			return response

	"""
	The seccond example is for whenever you are providing users with fixed downloads
	such as manuals etc. We do not only check if the file just exists, because that would
	allow an attacker to also download important other files from your server, so instead
	we whitelist them.
	"""
	
	def downloadStored(filename):

		response = Response(open(app.config['UPLOAD_FOLDER'] + filename).read())

		if whitelisting("file1.txt,file2.txt", $filename) != False:
			response.headers["Content-Description"] = "File Transfer"
			response.headers["Content-type"] = 'text/plain'
			response.headers["Content-Disposition"] = "attachment; filename=" + filename
			response.headers["Expires"] = 0
			response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
			response.headers["Cache-Control"] = "post-check=0, pre-check=0", false
			response.headers["Content-Length"] = os.path.getsize(filename)

			if os.path.exists(app.config['UPLOAD_FOLDER'] + filename):
        			return response
			