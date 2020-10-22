# Random password/token generation
-------

## Example:


	"""
	When needing to generate random numbers, always use proven methods 
	instead of writing your own.
	"""
	
	//Generate a strong security key
	app.secret_key = os.urandom(32)

	//A random string for generating WTF CSRF token
	app.config['WTF_CSRF_SECRET_KEY'] = base64.b64encode(rand.bytes(128))
    
