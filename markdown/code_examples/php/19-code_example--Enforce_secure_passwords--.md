
Enforce secure passwords
-------

**Example:**



    	<?php

	$pwd = $_POST['pwd'];

		//Recommended to use a small phrase instead of a password
		if(strlen($pwd) < 8 ) {
			$error .= "Password too short!";
			die;
		}
	
		//The password should include at least one number
		if(!preg_match("#[0-9]+#", $pwd) ) {
			$error .= "Password must include at least one number!";
			die;
		}

		//The password must at least include one letter
		if(!preg_match("#[a-z]+#", $pwd) ) {
			$error .= "Password must include at least one letter!";
			die;
		}

		//The password should at least include one CAPS
		if(!preg_match("#[A-Z]+#", $pwd) ) {
			$error .= "Password must include at least one CAPS!";
			die;
		}

		//The password should at least include one symbol
		if(!preg_match("#\W+#", $pwd) ) {
			$error .= "Password must include at least one symbol!";
			die;
		}

	/*
	Even though your password is sufficient to al your standards the password could still be a weak password
	Just imagine the password "Password!" could be easily guessed by an attacker. to prevent the use of weak passwords we 
	compare the password with a list of top 500 bad passwords and if matched, the password wil be rejected.
	*/
	$file = file_get_contents('badpasswords.txt');
   
	$pattern = explode(',', $file);
	
		foreach($pattern as $password)
		{
			if(preg_match($password, $pwd))
			{
				$error .= "Your password was matched with the bad password list, please try again.";
				die;
			}
		}

		if($error){
			echo "Password validation failure(your choise is weak): $error";
			die;
		} else {
			echo "Your password is strong.";
		}


	