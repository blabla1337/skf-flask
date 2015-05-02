
CSRF tokens
-------

**Example:**



    <?php

	//First after a succsesfull validation of a user login, the application must also start a session
	//which contains the "cross site request forgery" token.

	$_SESSION['csrf'] = base64_encode(openssl_random_pseudo_bytes(128));

	//The next step is implementing this random token in each form field as a hidden input parameter
	//and send it to a function which checks if the submitted token is equal to the one set after succesfull validation.
	?>


	<form method='post'><input type='text' name='value1' />
	<input type='text' name='value2' />    
	<input type="hidden" name="token" value="<?php echo $_SESSION['csrf']; ?>" id="token"></form>    

	<?php

	//here we are sending the token towards the function which does the token validation    
	protected function _checkCsrf($token){        
		session_start();                    
		
			if($_SESSION['csrf'] != $token){        
			    
				//Log the invalid token verification
				setLog($_SESSION['userID'],"invalid token: ".$_SERVER['HTTP_REFERER']."", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");
				
				//if the token was not valid we terminate the users session
				session_start();
				session_destroy();                   
				
				//The die function is to make sure the rest of the php code is not excecuted beyond this point
				die();        
			}    
	}     
	?>


	