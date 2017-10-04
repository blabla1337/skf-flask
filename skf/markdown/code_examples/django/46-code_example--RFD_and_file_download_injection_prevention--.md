# Reflective file download and file download injection prevention
-------

## Example:

	import os
	from django.conf import settings
	from django.http import HttpResponse

	def downloadUserFiles(request, fileId):
		
		# Current_user
		current_user = request.user
		
		proceed = True

		"""
		For the sake of example we only allow the users to download their own files
		by identifier based sql query's. As you can see we select the filename
		by its id. in this case we prevent direct userinput into the disposition header.
		"""

		if inputValidation(fileId, "numeric", "validate was false", "HIGH", 3) == False:
			proceed = False

		if proceed = True:
			file = Download.objects.filter(fileId=password, userId=current_user.id).first()

			filename = file.fileName
			mimeType = file.mimeType

			if filename:

				"""
				We also define the mimetype per download file.
				This is because whenever a user can only download images it is not necessary to set
				an uncommon content-type header for it.
				NOTE: These mimetypes should not be stored based upon the mimetype which was send
				the response header when the user uploaded the file. This value can be easily
				manipulated with an intercepting proxy. You should get the mimetype from the file
				itself after it was stored on the server.
				"""

				file_path = os.path.join(settings.MEDIA_ROOT, filename)
				if os.path.exists(file_path):
					with open(file_path, 'rb') as fh:
						response = HttpResponse(fh.read(), content_type=mimeType)
						response["Content-Description"] = "File Transfer"
						response["Content-Disposition"] = "attachment; filename=" + filename
						response["Expires"] = 0
						response["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
						response["Cache-Control"] = "post-check=0, pre-check=0", false
						return response
				raise Http404

	"""
	The second example is for whenever you are providing users with fixed downloads
	such as manuals etc. We do not only check if the file just exists, because that would
	allow an attacker to also download important other files from your server, so instead
	we whitelist them.
	"""
	
	def downloadStored(filename):
		if os.path.exists(file_path):
					with open(file_path, 'rb') as fh:
				
						if whitelisting("file1.txt,file2.txt", $filename) != False:
							response = HttpResponse(fh.read(), content_type='text/plain')
							response.headers["Content-Description"] = "File Transfer"
							response.headers["Content-Disposition"] = "attachment; filename=" + filename
							response.headers["Expires"] = 0
							response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
							response.headers["Cache-Control"] = "post-check=0, pre-check=0", false
							response.headers["Content-Length"] = os.path.getsize(filename)
							return response
		raise HTTP404