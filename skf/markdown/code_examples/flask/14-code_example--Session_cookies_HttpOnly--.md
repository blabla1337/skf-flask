# Session cookies HttpOnly
-------

## Example:


	"""
	Whenever a session is started, the "httpOnly" option should always be set to "true" or "1":
	"""
	
	from flask import Flask, session

	//Initialize the flask application
	app = Flask(__name__)

	//Name of the session cookie
	app.config['SESSION_COOKIE_NAME'] = 'hrj'

	//Path for the session cookie
	app.config['SESSION_COOKIE_PATH'] = '/'
	
	//Domain for the session cookie
	//Configure domains, do not use .yourdomain.com (wildcard)
	//This increases the attack surface!
	app.config['SESSION_COOKIE_DOMAIN'] = 'demo.yourdomain.com'
	
	//Controls if the cookie should be set with the secure flag
	app.config['SESSION_COOKIE_SECURE'] = True
	
	//Controls if the cookie should be set with the httponly flag
	app.config['SESSION_COOKIE_HTTPONLY'] = True
	
	//Lifetime of a permanent session
	app.config['PERMANENT_SESSION_LIFETIME'] = 3600

	//Store Value in session
	session['type'] = "value"
