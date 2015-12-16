
Password forget & Disallow old passwords
-------

**Example:**

    /*
	Whenever you are developing a password forget function, these are the steps to follow
	in order to create hardened defenses.
	
	
	 TABLE users
    -----------------------------------------------------------------     
    | userID | userName | password |   EmailAdress	 |    access	|
    -----------------------------------------------------------------    
    |   1	 | Admin	| Csdar323 | info@admin.com	 | 	   TRUE		|
    -----------------------------------------------------------------    	
    |	2	 | User		| Adf4fsv  | info@user.com   |	   FALSE	|
    -----------------------------------------------------------------    
    |	3	 | Guest	| dff4fKr  | info@guest.com	 |	   TRUE		|
    -----------------------------------------------------------------    


    TABLE passwordForget
    -----------------------------------------------------------------------------------------   
    | forgotPasswordID | 		Token 			 | 	UserID |   Active	|	  OlPasswords	|
    -----------------------------------------------------------------------------------------
    |        1	 	   | 	c3ab8ff13720e....	 |	  1	   | 	YES		|	   Csdar323		|
    -----------------------------------------------------------------------------------------
    |	     2	 	   | 	7dd39466b3c89....	 |	  1	   | 	NO		|		ef0c4f2		|
    -----------------------------------------------------------------------------------------
    |	     3	 	   | 	83d4a3960714c....	 |	  3	   | 	NO		|		dff4fKr		|
    -----------------------------------------------------------------------------------------
	
	
	As you can see we also store the old passwords into the password forget table, this
	we do in order to prevent the user from using old passwords later on in the process.
	
	Also use a cron job to make sure the generated tokens for the password reset are
	expire after a certain amount of time like 20 minutes.
	
	Now image the following forget password form:
	
	
	*/
	
	
	?>
	
	<h1>Forgot password?</h1>
	<form method='post'>
	Please enter your email adress:
	<input type='text' name="email"/>
	<input type='submit' name='submit'/>
	</form>	
	
	<?php
	
	
	
	if(isset($_POST['submit'])){
		
		checkValidity();
			
		}
	
	resetPassword();
	

	function checkValidity(){

		$stmt = $db->prepare("SELECT * FROM members WHERE email=?");
		$stmt->execute(array($_POST['email']));
		$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);
		
		foreach($rows as $row){
		
			//Here we select the old password as wel as the userid from the members table
			$password = $row['password'];
			$userID   = $row['id'];
			$email 	  = $row['email'];
		
		}
		
		//If the select was not empty we will be sending an email to the user as wel as
		//preparing the password forget function
		if(!empty($rows)){
		
			echo "An email was sent to your email for password reset";
			
			/*
			Before we do anything we first set all other posible active statuses to NO
			in order to prevent an attacker creating a whole lot of tokens and than fuzz 
			the password reset token. 
			*/
			
			$active = "NO";
			$stmt = $db->prepare("UPDATE forgetPassword SET active=? WHERE userID=?");
			$stmt->execute(array($active, $userID));
			$affected_rows = $stmt->rowCount();
			
			//Here we generate the password forget token
			$bytes = openssl_random_pseudo_bytes(30);
			$token = bin2hex($bytes);
			
			$stmt = $db->prepare("
			INSERT INTO forgetPassword 
				(token, userID, active, oldPasswords)
 					VALUES 
 						(?, ?, ?, ?)");
 			
 			$stmt->execute(array(
 			$token,
 			$userID,
 			'YES',
 			$password
 			));
 		
 			
 			//Here we send an email to the user with the needed reset function
 			$msg = "follow this link to reset your password http://example.com/index.php?resetLink=$token";
 			mail($email,"Password reset",$msg);
		}	
		
		else{
		
			/*
			We show the user the same message in order to prevent the enumeration of
			valid email adresses.
			*/
		
			echo "An email was sent to your email for password reset";			
		}
	}
	
	/*
	Imagine the user clicked on his link with the token included and is redirected towards
	the page where he can enter his new password.
	*/
	
	?>
	
	<h1>Please insert a new password</h1>
	<form method="post">
	type password:<br/>
	<input type="password" name='password'/><br/>
	verify password:<br/>
	<input type="password" name='password2'/>
	<br/>
	<input type='submit' name='change'/>
	</form>

	<?php
	
	//On submit will call the function of resetPassword:
	if(isset($_POST['change'])){
		resetPassword();
	}
	
	function resetPassword(){
									
			/*
			Now we select the information from the forgot password function where the
			forgot tokens matches the token in the database.
			*/
			
			$active = "YES";
		
			$stmt = $db->prepare("
			SELECT  a.userID, a.token, b.id 
					FROM forgetPassword as a
						JOIN members as b
							ON a.userID = b.id WHERE token=? and Active=? ");
						
			$stmt->execute(array($_GET['resetLink'], $active));
			$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);

			foreach($rows as $row){

				//Here we select token and users id:
				$token  = $row['token'];
				$userID = $row['userID'];	
		
			}
			
			if($token === $_GET['resetLink']){
			
				/*
				First we pull the password through our function which enforces the input of
				secure passwords.(see "Enforce secure passwords" in code examples for more
				detailed information)
				*/
			
				if(enforceSecurePassword($_POST['password']) === true);
		
				/*
				Than we encrypt our password 
				(see "Password storage" in code examples for more
				detailed information)
				*/
			
				$newPassword = encryptPassword($_POST['password']);
			
				/*
				Finally we compare the password against other old passwords from the 
				pasword reset database in order to prevent the user from using old passwords 
				which could already be comprimised by any means.
				*/
			
				$stmt = $db->prepare("SELECT oldPasswords FROM forgetPassword where userID=?");
				$stmt->execute(array($userID));
				$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);

				foreach($rows as $row){
			
					if($newpassword === $row['oldPasswords']){
						echo "This was an old password please do not use this password";
						die();
					}else{
						
						//First we update the new password for the user
						$active = "NO";
						$stmt = $db->prepare("UPDATE members SET password=? WHERE userID=?");
						$stmt->execute(array($newPassword, $userID));
						$affected_rows = $stmt->rowCount();
						
						//Then we destroy the reset token by setting it's value to NO
						$stmt = $db->prepare("UPDATE forgetPassword SET active=? WHERE userID=?");
						$stmt->execute(array($active, $userID));
						$affected_rows = $stmt->rowCount();
					
					}
				
				}	
			}
		}
	
	}	
	
	?>