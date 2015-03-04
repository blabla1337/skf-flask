
Session cookies (domain)
-------

**Example:**



    	<?php

	//Whenever a session is started, and you want to share it over different domains, the domain value should be set:

	public function sessionStart(){

	$lifetime = 3600;
	$path     = "/";
	$domain   = ".yourdomain.com";  // <--  the Configure domains

	$secure   = 0;
	$httponly = true;

	session_set_cookie_params($lifetime, $path, $domain, $secure, $httponly);

	?>


	
