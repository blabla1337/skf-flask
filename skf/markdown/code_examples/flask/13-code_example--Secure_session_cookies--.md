# Secure session cookies
-------

## Example:


    """
    If you use SLL you can also make your cookies secure (encrypted) to 
    avoid "man-in-the-middle" cookies reading
	"""

	from flask import Flask, session

	//Initialize the flask application
	app = Flask(__name__)

	//Set the secret key.  keep this really secret:
	app.secret_key = open("/dev/random","rb").read(32) 

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
