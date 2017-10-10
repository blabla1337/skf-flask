# System commands
-------

## Example:


	"""
	Define the whitelist pattern and validation type and input parameter like:
	getFiles("value1,value2,etc", "alphanumeric", $_GET['filename'], "3")
	"""

	def command(whiteListPattern, validationType, inputParameter){

		continue = True

		"""
		Whenever a system command is finished, you should properly sanitize and escape this user input.
		System command functions examples are: system(), eval(), exec()

		First, we want to filter the filenames for expected values. For this example we use only a-z/0-9
		Whenever the values are tampered with, we can assume an attacker is trying to inject malicious input.
		for more information about validation see "input validations" in the code examples:
		"""

		if inputValidation(inputParameter, validationType) == False:
			continue = False

			"""
			Second, we want to whitelist the filenames for expected values, in this example they are,
			page1,page2 etc.. for more information about whitelisting see "white-listing" in the code examples:
			"""

		if whitelisting(whiteListPattern, inputParameter) == False:
			continue = False

		# If all went good we include the filename
		if continue == True:

			# Even though there is match we still escape the shelx.quote():
			command = './configure {}' .format(quote(inputParameter))
			os.system(command)
