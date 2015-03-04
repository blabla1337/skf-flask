
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

	?>


	