# Password storage(salting/stretching/hashing)
-------

## Example:


    <?php

	class passwordHash{
		
		public function createHash($pwd){

			/*
			For the encryption of passwords we use PHP's BCRYPT encryption method.
			*/

			//Here we generate a hash with a random salt
			public function HashPassword($password){
				$options = [
				'cost' => 11,
				'salt' => mcrypt_create_iv(22, MCRYPT_DEV_URANDOM),
				];

				$hash =	password_hash($password, PASSWORD_BCRYPT, $options)."\n";

				return $hash;
			}

			//Validate your password
			public function ValidatePassword($correctHash, $password)
			{
			if(password_verify($password, $correctHash))
				{
					//After successful validation we want to log that password was validated successfully:
					setLog($_SESSION['userID'],"Password return true", "SUCCESS", date(dd-mm-yyyy), $privilege, "NULL");
					return true;
				}else{		
					//We log invalid password use
					setLog($_SESSION['userID'],"Password return false", "FAIL", date(dd-mm-yyyy), $privilege, "LOW");
					return false;
				}
			}
		}
	}
			
	?>
