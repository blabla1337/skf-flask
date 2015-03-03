
Password storage(salting/stretching/hashing)
-------

**Example:**



    	<?php

	//Takes a password and returns the salted hash
	//returns - the hash of the password
	function HashPassword($password){
		
	    $salt = bin2hex(mcrypt_create_iv(32, MCRYPT_DEV_URANDOM)); //get 256 random bits in hex
	    $hash = hash("sha256", $salt . $password); //prepend the salt, then hash
	    //store the salt and hash in the same string, so only 1 DB column is needed
	    $final = $salt . $hash;
	    return $final;
	}
	
	//Validates a password
	//returns true if match correct
	function ValidatePassword($correctHash, $password){
		
	    $salt = substr($correctHash, 0, 64); //get the salt from the front of the hash
	    $validHash = substr($correctHash, 64, 64); //the SHA256
	    $testHash = hash("sha256", $salt . $password); //hash the password being tested
	
	    //if the hashes are exactly the same, the password is valid
	    return $testHash === $validHash;
	}

	?>



	