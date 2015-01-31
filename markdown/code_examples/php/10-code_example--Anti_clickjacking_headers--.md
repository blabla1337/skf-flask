
Anti clickjacking headers
-------

**Example:**



		/*
	There are two options for setting the anti-clickjacking headers in your application
	*/

	//will prevent your page completely from being displayed in an iframe.
	header('X-Frame-Options: DENY');


	//will prevent you page from being displayed in other sites in an iframe.
	header('X-Frame-Options: SAMEORIGIN');
	




	