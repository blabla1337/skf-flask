# Random password/token generation
-------

## Example:


	"""
	When needing to generate random numbers, always use proven methods 
	instead of writing your own.
	"""
	
	import secrets
	SECRET_KEY = secrets.token_hex(36)
    
	"""
	use secrets.token_urlsafe() for base64 encoded random secure strings
	"""


