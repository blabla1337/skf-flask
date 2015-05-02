
Timeout a session
-------

**Example:**



    <?php

	public function sessionStart(){

		$lifetime = 3600; // <-- lifetime of a session
		$path     = "/";
		$domain   = "";
		$secure   = 0;
		$httponly = true; 

		session_set_cookie_params($lifetime, $path, $domain, $secure, $httponly);

	}
	
	/*
	You could also set the session cookie its secure function with a ini_set
	This ini_set has to be included in the header of al your pages in order to work
	*/
	
    ini_set('session.cookie_lifetime', 3600);

	?>


	