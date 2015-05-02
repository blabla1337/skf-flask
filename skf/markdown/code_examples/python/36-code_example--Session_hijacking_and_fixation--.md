
Session hijacking and session fixation
-------

**Example:**

   	<?php

	/*
	As soon as a user logs into your application you must store his session id as wel as his
	IP adress allong with his userID. This information will be used later on in your application in order to
	identify possible session hijacking.

	TABLE track_sessions
	---------------------------------------------------------------------------------
	| TrackID | userID |		   	   SESSION 		            |     Ip adress	    | 
	---------------------------------------------------------------------------------
	|   1     | 1      | 	79dcd529c0f5e01a9bfb2425c52036c6    |	123.45.67.89	|   
	---------------------------------------------------------------------------------
	|   2     | 1      | 	79dcd529c0f5e01a9bfb2425c52036c6    |	123.45.67.81	|
	---------------------------------------------------------------------------------
	|   3     | 2      | 	c80959d3ea4c166413774e45375ac2a1    |	987.65.43.21	|
	---------------------------------------------------------------------------------

	In order to prevent session hijacking there are a couple of defense strategies
	which combined are a hardened defense.  
	*/

	/*
	First we implement the strict transport security header, this is in order to prevent
	users from accessing your application over an unprotected connection.
	*/

	//Example of the strict transport security header:
	header('Strict-Transport-Security: max-age=31536000');


	//If all present and future subdomains will be HTTPS:
	header('Strict-Transport-Security: max-age=31536000; includeSubDomains');

	/*
	Recommended: If the site owner would like their domain to be included in the HSTS preload 
	list maintained by Chrome (and used by Firefox and Safari), then use:
	*/

	header('Strict-Transport-Security: max-age=31536000; includeSubDomains; preload');

	/*
	The `preload` flag indicates the site owner's consent to have their domain preloaded. 
	The site owner still needs to then go and submit the domain to the list. the preload list
	enforces the browser to always present your application on HTTPS even on the first time
	the user hits your application
	*/

	/*
	Then we set the httpOnly flag
	(see "HttpOnly" in the code examples for more details about implementation)
	*/
	ini_set('session.cookie_httponly', 1);

	/*
	Then we set the flag for session timeout
	(see "Timeout" in the code examples for more details about implementation)
	*/
	ini_set('session.cookie_lifetime', 3600);

	/*
	Then we set the session secure flag 
	(see "Secure flag" in the code examples for more details about implementation)
	*/
	ini_set('session.cookie_secure', 1);

	/*
	On login we change the session id in order to prevent session fixation
	(see "Login functionality" in the code examples for more details about implementation)
	*/
	session_regenerate_id(true);

	/*
	NOTE: On applications that require high level security, there should never be an
	remember me functionality implemented.
	*/


	/*
	Now imagine the scenario after the login of the user (see the "login functionality" in
	the code examples for more details). Whenever the user is logged in, the users ip adress 
	and session id are also stored in the database these values are used in order to verify 
	if there are mulitple users active on the same session. 
	If so, we can let the user decide to terminate the session and terminate the
	other assigned sessions.
	*/
	 
	 //We implement this logic into our checksession functionality
	 function _checkSession(){

			//Here we check for a valid session to see if the user is authenticated
			session_start();
			if(($_SESSION['access'] != "active") || $_SESSION['access'] == ""){
				header("Location: /login");
				die();
			}

		/*
		Then we start the rest of the function where we will check if there are multiple
		users/ip adresses using the same session id
		*/

		//store current session id
		$session  = session_id();

		//get users ip adres
		$ipadress = $_SERVER['REMOTE_ADDR'];

		$stmt = $db->prepare("SELECT * FROM track_sessions WHERE userID=:id");
		$stmt->execute(array(':id' => $_SESSION['userID']));
		$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);

			foreach($rows as $row){
		
				//check to see if the current ip adress matches the one stored in login if not warn user!
				if(($ipadress != $row['ipadres']) && $row['SESSION'] != $session){
		
					echo "
					<div style='border-style:solid; border-color:black; color:white; background-color:red; text-align:center; float:left;'>
					<p>There are other active sessions on other ip-adresses.<br/>
					Your session could be hijacked press logout in order to authenticate again
					for security reasons!
					<br/><br/>
					<a href='/logout'>Terminate sessions</a>
					<br/>
					<a href='/Proceed'>Proceed anyway</a>
					</p>
					</div>
					";				
				}	

			}			
	}

	/*
	the only thing left to do now is to update your track_sessions table by inserting
	the ipadress, sessionID and userID if you want to accept the other sessions as valid.
	Otherwise the user just has to terminate his current session in order to lock out the
	other sessions.
	*/

	?>

