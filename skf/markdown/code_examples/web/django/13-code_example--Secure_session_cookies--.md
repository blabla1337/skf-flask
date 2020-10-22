# Secure session cookies
-------

## Example:

    
    """
    If you use SLL you can also make your cookies secure (encrypted) to 
    avoid "man-in-the-middle" cookies reading with

    For using sessions edit the middleware and make sure it contains 'django.contrib.sessions.middleware.SessionMiddleware'

    For adding HTTPONLY Cookies, we have to add the line in settings.py
    SESSION_COOKIE_HTTPONLY = True

    For adding Session Cookie age, we have to add the line in settings.py
    SESSION_COOKIE_AGE = 60000

    For setting session cookie domain, we have to add the line in settings.py
    SESSION_COOKIE_DOMAIN = 'demo.yourdomain.com'

	For setting session cookie name, we have to add the line in settings.py
	SESSION_COOKIE_NAME = 'demo'    
	
	For setting session cookie path, we have to add the line in settings.py
	SESSION_COOKIE_PATH = '/'

	For setting session cookie path, we have to add the line in settings.py
	SESSION_COOKIE_SECURE = True
	"""

	//For adding session cookie
	request.session['test'] = 'test'