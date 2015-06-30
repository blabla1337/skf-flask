CSRF tokens
-------

**Example:**


    <?php
	class CSRF{
	
		public function generateToken(){
            /*
            After successful user authentication, the application must start a session
			which contains the "Cross Site Request Forgery(CSRF)" token.
            */

            $_SESSION['csrf'] = base64_encode(openssl_random_pseudo_bytes(128));
		}
		
		/*

        The random CSRF token generated need to be send to the server with every form submission.
        This token is included in a form as a HTML hidden form field parameter. When the form is 
        submitted the token value is also submitted along with it. 
        
        The token is then validated against the csrf token which was generated during user authentication. 
        Below code demonstrate the validation of csrf token at the server side:

		*/

		protected function _checkCsrf($token){        
			session_start();                    
		
			if($_SESSION['csrf'] != $token){        
			
				//Log the invalid token verification
				setLog($_SESSION['userID'],"invalid CSRF token send!", "FAIL", date("d-m-y"), $_SESSION['privilege'], "HIGH");
			
				//If the token was not valid we terminate the users session
				session_start();
				session_destroy();                   
			
				//The die function is to make sure the rest of the php code is not excecuted beyond this point
				die();        
			}    
		}  
	}   
	?>


	
