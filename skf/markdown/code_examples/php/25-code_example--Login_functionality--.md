# Login functionality
-------

## Example:


    <?php

	/*
	For privilege based authentication we need an extra table in your database in order to write the users privileges to.

	TABLE users
	---------------------------------------------------------------------------------    
	| userID | userName | password | privilegeID |    access	| AggregateControl	|
	---------------------------------------------------------------------------------   
	| 1	     | Admin    | Csdar323 |      1	     | 	 TRUE       |       2336        |
	---------------------------------------------------------------------------------   	
	| 2      | User	    | Adf4fsv  |      2	     |   FALSE	    |         0	        |
	---------------------------------------------------------------------------------   
	|	3	     | Guest	  | dff4fKr  |	  3		     |	   TRUE		|		135			          |
	---------------------------------------------------------------------------------   

	TABLE privileges
	----------------------------------   
	| privilegeID | privilege        |
	----------------------------------
	|     1       | edit:read:delete |
	----------------------------------
	|     2	      | edit:read        |
	----------------------------------
	|     3       | read             |
	----------------------------------

	Now instead of using roles in sessions we rather want to assign privileges to users
	by means of a Database-Based Authentication system.
	Now we can easily assign a user certain privileges for him to access.
	See "Privilege based authentication" code example for more information:
	*/

	class login{
		public function loginUser($username,$password)
		{

			//init DB connection
			include("classes.php");
			$conn = new database();
			$db = $con->connection();

			/*
			You must log invalid user input in order to detect a possible attack on your login form
			In this example the expected input is "a-Z/0-9 - _"
			*/

			if(preg_match("/[^a-zA-Z0-9]/", $username))
			{       
				//Set a log for whenever there is unexpected user input with a threat level
				setLog("null","invalid expected input", "FAIL", date("d-m-y"), "null", "HIGH");
				header("location:login.php");
				die();
			}

			/*
			We also want to make sure the user access is TRUE, if not, it means the user was blocked
			for attempting to hack the application
			*/

			//After successful validation we want to log that username was validated successfully:
			setLog($_SESSION['userID'],"Username return true", "SUCCESS", date(dd-mm-yyyy), $privilege, "NULL");

			//PDO prepared statement in order to prevent SQL injections
			$stmt = $db->prepare("
				SELECT a.username, a.password, a.privilegeID, b.privilegeID, b.privilege   
					FROM users as a
						JOIN privileges as b
							ON a.projectID = b.projectID
								WHERE a.username = :username and b.access='TRUE'");

			$this->_setSql($sql);

			$stmt->execute(array(':page' => $_GET['page'], ':username' => $username));
			$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);

			foreach($rows as $loginUser){

				/*
				Than we validate the password, if the validation is true than we set the sessions
				For more detailed information on password validation check please look into the
				Password storage(salting/stretching/hashing) in the knowledge-base for more information.
				*/
				if($this->ValidatePassword($loginUser['password'], $password) === true)
				{
					//After successful validation we want to log that Password was validated successfully:
					setLog($_SESSION['userID'],"Password return true", "SUCCESS", date("d-m-y"), $privilege, "NULL");

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
					return $loginUser;
				}
			}
		}
	}

    ?>
