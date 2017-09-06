# Enforce secure passwords
-------

## Example:


    <?php

	class passwordPolicy{
		public function createPassword($pwd){
			$proceed = true;

			//Recommended to use a small phrase instead of a password:
			if(strlen($pwd) < 8 ){
				$error .= "Password too short!";
				$proceed = false;
			}

			$pattern = array("/[0-9]+/","/[a-z]+/","/[A-Z]+/","/\W+/");		

			/*
			The password should include at least one number, a small letter, a CAPS,
			and a special character as defined in the patterns array:
			*/
			foreach($pattern as $value){
				if(!preg_match($value, $pwd)){
					$error .= "Password incomplete";
					$proceed = false;
				}
			}

			/*
			Even though your password is sufficient according to all your standards, the password could still be weak.
			Just imagine the password "Password!"; this could easily be guessed by an attacker. To prevent the use of weak passwords we
			compare the password with a list of top 500 bad passwords and if matched, the password wil be rejected:
			*/
			$file = file_get_contents('badpasswords.txt');

			$pattern = explode(',', $file);

			foreach($pattern as $password){
				if(preg_match($password, $pwd)){
					$error .= "Your password was matched with the bad password list, please try again.";
					$proceed = false;
				}
			}

			if($proceed == true){
				echo "Your password is allowed!";
				return true;
			}else{
				echo "Password validation failure(your choice is weak): $error";
				return false
			}				
		}
	}
			
    ?>
