
Secure session cookies
-------

**Example:**



    	<?php

	/*
	Whenever  a cookie is send over a secured connection, the cookie should be set
	with the secure flag in order to guarantee the integrety of the data it contains.
	the secure flag is set by giving it the true or 1 value
	*/

	public function sessionStart(){


	$lifetime = 3600;
	$path     = "/";
	$domain   = "";
	$secure   = true; // <-- the secure flag
	$httponly = true; 


	session_set_cookie_params($lifetime, $path, $domain, $secure, $httponly);

	?>


	