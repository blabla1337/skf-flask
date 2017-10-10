# XSL injection prevention
-------

## Example:


    """
		In order to prevent XSL injections you must enforce strict policy's whenever the
		files are loaded from a source controlled by an possible attacker.

		Let's say for example that the user can choose from several XSL files on your application.

		ABC.xsl arranges your employee names on alphabetical order
		CBA.xsl does not care and just shows the input by order of your XML file.

		Before we want to attach the XSL files to the style sheet we first want to
		do validation on the request to make sure the included file was one of our own pre
		defined files, example:
		including("file1.xsl,file2.xsl", filename)
	"""

	def including(whiteListing, input):

		continue = True

		"""
		We want to whitelist the paged for expected values, in this example they are,
		page1,page2 etc.. for more information about whitelisting see "white-listing" in the code examples:
		"""

		if whitelisting(whiteListing, input, count) == False:
			continue = False

		# If all went good we do the function
		if continue == True:
			#Load XML file
			root = etree.parse("test.xml")

			xslt_root = etree.XML(input)
			transform = etree.XSLT(xslt_root)

			# Transform the XML
			result_tree = transform(root)

		else:

			return False
