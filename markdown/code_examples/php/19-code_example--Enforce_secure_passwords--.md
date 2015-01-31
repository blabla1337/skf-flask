
Enforce secure passwords
-------

**Example:**



		$pwd = $_POST['pwd'];

		//Recommended to use a small phrase instead of a password
		if( strlen($pwd) < 20 ) {
			$error .= "Password too short!";
			die;
		}

		if( !preg_match("#[0-9]+#", $pwd) ) {
			$error .= "Password must include at least one number!";
			die;
		}


		if( !preg_match("#[a-z]+#", $pwd) ) {
			$error .= "Password must include at least one letter!";
			die;
		}


		if( !preg_match("#[A-Z]+#", $pwd) ) {
			$error .= "Password must include at least one CAPS!";
			die;
		}



		if( !preg_match("#\W+#", $pwd) ) {
			$error .= "Password must include at least one symbol!";
			die;
		}


		if($error){
			echo "Password validation failure(your choise is weak): $error";
			die;
		} else {
			echo "Your password is strong.";
		}



	