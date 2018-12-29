# Session hijacking and fixation 
-------

## Example:

	/*
	First we implement the strict transport security header, this is in order to prevent
	users from accessing your application over an unprotected connection.
	*/

	//Example of the strict transport security header:
	// response.setHeader("Strict-Transport-Security", "max-age=31536000");


	//If all present and future subdomains will be HTTPS:
	//response.setHeader("Strict-Transport-Security", "max-age=31536000; includeSubdomains;");

	/*
	Recommended: If the site owner would like their domain to be included in the HSTS preload 
	list maintained by Chrome (and used by Firefox and Safari), then use:
	*/

	// response.setHeader("Strict-Transport-Security", "max-age=31536000; includeSubdomains; preload");

	/*
	The `preload` flag indicates the site owner's consent to have their domain preloaded. The preload list
	enforces the browser to always present your application on HTTPS even on the first time
	the user hits your application
	*/

	/*
	Then we set the httpOnly flag
	(see "HttpOnly" in the code examples for more details about implementation)
	*/

	/*
	Then we set the flag for session timeout
	(see "Timeout" in the code examples for more details about implementation)
	*/

	/*
	Then we set the session secure flag 
	(see "Secure flag" in the code examples for more details about implementation)
	*/

	/*
	On login we also add another cookie with a random value to the application in order to
	prevent an attacker to fixate an JSSESSION id on your users and hijack their sessions
	(This code example can be found in the "Login functionality" for more detailed information)
	*/

	/*
	Now imagine the scenario after the login of the user (see the "login functionality" in
	the code examples for more details). Whenever the user is logged in, the users ip address, 
	user agent string and session id are also stored in the database these values are used in order to verify if there are multiple users active on the same session. 
	If so, we can let the user decide to terminate the session and terminate the
	other assigned sessions.
	*/
	function login(**args**) 
		{
		/* Passport prevents session fixation but doesn't track concurrent long lived sessions, this is custom code on top of passport
		*/
		}