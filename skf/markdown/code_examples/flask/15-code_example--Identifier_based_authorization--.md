# Identifier-based authorization
-------

## Example:


    """
    Define the whitelist pattern and validation type and input parameter like:
    identity("page1,page2", "alphanummeric", $_GET['page'])
    """

    def identity(whiteListPattern, validationType, inputParameter):

    	continue = True

    	"""
    	First, we want to filter the filenames for expected values. For this example we use only a-z/0-9
    	Whenever the values are tampered with, we can assume an attacker is trying to inject malicious input.
    	for more information about validation see "input validations" in the code examples:
    	"""

    	if inputValidation(inputParameter, validationType, "Invalid userinput", "HIGH", countLevel) == False:
            continue = False

    	"""
    	Second, we want to whitelist the filenames for expected values, in this example they are,
    	page1,page2 etc.. for more information about whitelisting see "white-listing" in the code examples:
    	"""

    	if whitelisting(whiteListPattern, inputParameter) == False:
            continue = False

    	"""
    	Whenever you are checking whether a user is restricted to review certain data,
    	the access restrictions should be processed serverside.
    	The userID could be stored inside a session variable on login, and should be used to
    	retrieve userdata from the database:
    	"""
    	
        if continue == True : 

    		"""
    		We count the number of connections towards the database,
    		See "aggregate usercontrolls" code example for more information:
    		"""

            countAccess(1)
            data = Table.query.filter_by(id=session['id'], page=inputParameter).first()

            return data

        else:

            return False