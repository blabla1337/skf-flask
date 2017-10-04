# Re-authentication
-------

## Example:


    <?php

	/*
	Whenever a user wants to change his credentials or do other important data exchanges such as
	transferring money he should always be challenged to re-authenticate himself before
	allowing them to perform these actions.
	*/

	class challengeUser{
			public function reauthenticate($password){

			//init DB connection
			include("classes.php");
			$con     = new database();
			$logging = new logging();

			$db = con->connection();

			//PDO prepared statement in order to prevent SQL injections        
			$stmt = $db->query("SELECT * FROM members WHERE id = :userID ");

			//We than bind the parameters in order to prevent SQL injection;
			$stmt->execute(array(':userID'=>$_SESSION['userID'] ));


			$loginUser = $stmt->fetchAll(PDO::FETCH_ASSOC);

			/*
			Than we validate the password, if the validation is true than we set the sessions
			For more detailed information on password validation check please look into the
			Password storage(salting/stretching/hashing) in the knowledge-base for more information.
			*/
			if($this->ValidatePassword($loginUser['password'], $password) === true){

				//After successful validation we want to log that Password was validated successfully:
				setLog($_SESSION['userID'],"Password return true", "SUCCESS", date(dd-mm-yyyy), $privilege, "NULL");

				session_start();

				//Change the session id on login
				session_regenerate_id(true);

				//Here we set a session to see if the user is authenticated throughout the system
				$_SESSION['access']   = "active";

				/*
				The userID in a session variable to use as an identifier to prevent a user reading
				into unauthorized data, See Identifier-based authorization for more information and
				code examples.
				*/

				$_SESSION['userID']   = $loginUser['id'];

				//The CSRF token is set here by an approved random number generator
				$_SESSION['csrf'] = base64_encode(openssl_random_pseudo_bytes(128));

				//if all is ok we return loginUser values
				return true;

			}else{

				//The user failed re-authenticating himself
				$logging->setLog($_SESSION['userID'],"Re-authentication failed", "FAIL", date("d-m-y"), "null", "MOD");

				//If the authentication fails we destroy the session
				session_start();
				session_destroy();

				//Regenerate the session ID to lock out an attacker!
				session_regenerate_id(true);
				$_SESSION['active'] = "";

				header("location:login.php");

				die();           	
			}
		}
	}

	/*
	Before we let a user perform certain actions he should first be challenged to authenticate
	himself. imagine the following scenario, the user wants to change his email address.
	*/

	$challenge =  new challengeUser()
	if($challenge->reauthenticate() !== true){

		echo "please reauthenticate yourself";
		echo
		"
		<form method='post'>
		<input type='password' name='password'/>
		<input type='submit' name='authenticate'/>
		</form>		
		";

	}else{

		//Do operation for changing the email address
		echo "You can now change your email address!";
	}

    ?>
