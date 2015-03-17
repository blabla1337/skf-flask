
Session cookies (domain)
-------

**Example:**



    <?php

	//Whenever a session is started, and you want to share it over different domains, the domain value should be set to the specific domain:

	public function sessionStart(){

	$lifetime = 3600;
	$path     = "/";
	$domain   = "demo.yourdomain.com";  // <--  the Configure domains, do not use .yourdomain.com (wildcard) this increases the attack surface!

	$secure   = 0;
	$httponly = true;

	session_set_cookie_params($lifetime, $path, $domain, $secure, $httponly);

	?>


	
