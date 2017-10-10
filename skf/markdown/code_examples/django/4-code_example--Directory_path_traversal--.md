# Directory/path traversal
-------

## Example:

	"""
	Define the whitelist pattern and validation type and input parameter, countLevel like:
	getFiles("images,css,js", "alphanumeric", foldername)
	"""

	def getFiles(request, whiteListPattern, validationType, inputParameter):

		continue = True
        
        """
		First, we want to filter the filenames for expected values. For this example we use only a-z/0-9 - alphanumeric
		Whenever the values are tampered with, we can assume an attacker is trying to inject malicious input.
		for more information about validation see "input validations" in the code examples:
		"""
		
		if inputValidation(inputParameter, validationType) == False:
			continue = False

		"""
		Second, we want to whitelist the filenames for expected values, in this example they are,
		page1,page2 etc.. for more information about whitelisting see "white-listing" in the code examples:
		"""

		# Check for filename Whitelisting
		if whitelisting(whiteListPattern, inputParameter):
			continue = False

		if continue == True:
        	# Create Path
        	path = os.path.join(settings.MEDIA_ROOT, inputParameter)   
        	images = []

        	# List all the URL
        	for f in os.listdir(path):
            	if f.endswith("jpg") or f.endswith("png"):
                	images.append("%s%s/%s" % (settings.MEDIA_URL, inputParameter, f))
        
        	return render_to_response('gallery.html', {'images': images})

        else:

			return render_to_response('gallery.html', {'images': ''})        	

    # gallery.html

    {% for image in images %}
    <img src='{{image}}' />
    {% endfor %}