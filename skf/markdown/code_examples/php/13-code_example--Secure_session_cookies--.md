
Secure session cookies
-------

**Example:**


    <?php

	/*
	Whenever  a cookie is sent over a secured connection, the cookie should be set
	with the secure flag, in order to guarantee the integrity of the data it contains.
	The secure flag is set by giving it the "true" or "1" value:
	*/

	public function sessionStart(){


		$lifetime = 3600;
		$path     = "/";
		$domain   = "";
		$secure   = true; // <-- the secure flag
		$httponly = true; 


		session_set_cookie_params($lifetime, $path, $domain, $secure, $httponly);
	}
	
	/*
	You could also set the session cookie its secure function with a ini_set
	This ini_set has to be included in the header of al your pages in order to work
	*/
	
	ini_set('session.cookie_secure', 1);

	?>


	
