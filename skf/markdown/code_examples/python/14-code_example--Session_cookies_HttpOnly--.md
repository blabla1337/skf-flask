
Session cookies HttpOnly
-------

**Example:**


    <?php

	//Whenever a session is started, the "httpOnly" option should always be set to "true" or "1":

	public function sessionStart(){

		$lifetime = 3600;
		$path     = "/";
		$domain   = "";
		$secure   = 0;
		$httponly = true; // <--  the httponly flag


		session_set_cookie_params($lifetime, $path, $domain, $secure, $httponly);
	}
	
	/*
	You could also set the session cookie its httpOnly function with a ini_set
	This ini_set has to be included in the header of al your pages in order to work
	*/
	
	ini_set('session.cookie_httponly', 1);
	
	

	?>
