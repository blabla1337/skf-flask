
User registration / Sql truncation prevention
-------

**Example:**

   		<?php

	/*
	In order to prevent Column truncation sql injection Solution we have to make sure the
	applications structural logic does not mismatches with the database structural logic.
	To achieve this imagine the follow example of a database structur of a users table
	
	TABLE users
	------------------------------------------------------------
	|	     *Name* 	   |	*Type* 		  |    *Extra*     |
	------------------------------------------------------------
	|        userID	       |    Int(11)       | AUTO_INCREMENT |
	------------------------------------------------------------
	|       Username  	   |    char(21)      |  			   |
	------------------------------------------------------------
	|       Password       |  Varchar(255)    |				   |
	------------------------------------------------------------
	|      PrivilegeID     |    Int(11)       | 			   |
	------------------------------------------------------------
	*/
	
	class registerUser{	
		//First we create a function in order to select all usernames in order to see of they already exsists
		public function userCheck($username){
			
			//init DB
			$con = new database();
			$db = $con->connection();
			
			$stmt = $db->prepare("SELECT * FROM members WHERE username = :input");
			$stmt->bindParam(':input', $username, PDO::PARAM_STR);
			$stmt->execute();
	
			if($stmt->fetch(PDO::FETCH_OBJ) == False){ 
				//Return true in order to complete registration
				return true;
	
			}else{
				//The username already exists:
				return false;
			}
		}
		
		public function userRegister($username, $password, $privID){
			
			//init DB
			$con  = new database();
			$user = new registerUser();
			$db = $con->connection();
			
			/*
			Whenever the user gains the abbility to register himself or change his user
			credentials you must always enforce the application to compare the length of the
			submitted string against the length of the allowed string length in your database
			structure in order to prevent sql column truncation.
			*/
			$length = strlen($username);
		
			/*
			We now compare the length of the username against the allowed string length in
			The database structure
			*/
	
			if($length >= 21){
				//If length is to large the application must die.
				die("Username was to long!");	
			}
		
			//If true than register the user!		
			if($user->Usercheck($username) === true){
				
				$hash = new passwordHash();
	
				//Than we encrypt the password with the B-crypt encryption function of PHP
				$hash->createHash($password);
	
				//After succesful validation we enter the new user into the database
				$stmt = $db->prepare(

				"INSERT INTO users 
							(Username, Password, PrivilegeID)
						VALUES 
							(?, ?, ?)");
			
				$stmt->execute(array($username, $hash, $privilegeID));
				$affected_rows = $stmt->rowCount();			
			}else{
				echo "Username already existed";
			}
		}	
	}
	
	?>

