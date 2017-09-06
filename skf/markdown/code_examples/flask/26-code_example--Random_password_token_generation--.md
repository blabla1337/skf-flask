# Random password/token generation
-------

## Example:


	"""
	When needing to generate random numbers, always use proven methods 
	instead of writing your own.
	"""
	
	//Return a 50 character random string usable as a SECRET_KEY setting value.
	from django.core.management.utils import get_random_secret_key
	SECRET_KEY = get_random_secret_key()
	
	//Generate an even longer random string usable as a SECRET_KEY setting
	from django.utils.crypto import get_random_string
	chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
	SECRET_KEY = get_random_string(100, chars)
    
