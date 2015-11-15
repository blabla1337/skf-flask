
Random password/token generation
-------

**Example:**



    <?php

	//A good random token example for tokens would be:
	$_SESSION['csrf'] = base64_encode(openssl_random_pseudo_bytes(128));

	//A good random password would be: 
	$bytes = openssl_random_pseudo_bytes(15);
	$pwd = bin2hex($bytes);

	?>


	
