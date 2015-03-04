
System commands
-------

**Example:**



	    <?php

		/*
		Whenever a system command is finished, you should properly sanitise and escape this user input.
		System command functions examples are:
		system()
		eval()
		exec()
		*/

			 //First we want to filter the filenames for expected values, for this example we use only a-z/0-9
			 //Whenever the values are tampered with, we can assume an attacker is trying to inject malicious inpuatt
			if(!preg_match("/^[a-zA-Z0-9]+$/", $_POST['configure_options']){

					/*
					Set counter; if counter hits 3, the user's session must terminated.
					After 3 session terminations the user's acount must be blocked.
					Given the high threat level, there will be immediate session termination:
					*/
					setCounter(3);
			
					//Set a log for whenever there is unexpected user input with a threat level:
					setLog($_SESSION['userID'],"invalid expected input", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");
				}
	 

		//Secondly, we define the allowed arguments
		$whiteList = "/allowed argument/";

		//Next we validate the incoming user input in a preg_match function
		$sanitised = preg_match($whiteList, $_POST['configure_options'], $matched);

			//If there is a match we can proceed 
			if($matched){

				//Even though there is a match we still escape the shellcommand:
				$command = './configure '.$sanitised;
				$escaped_command = escapeshellcmd($command); 
		
				//Only after validation do we put the shellcommand into the system() function:
				system($escaped_command); 
			} else {		
					/*
					Set counter; if counter hits 3, the user's session must be terminated.
					After 3 session terminations the user's acount must be blocked.
					Given the high threat level there will be immediate session termination:
					*/
					setCounter(3);
			
					//Set a log for whenever there is unexpected userinput with a threat level:
					setLog($_SESSION['userID'],"Possible command injection attack on system function", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");        
					die(); 
			
				  }
			 }

		?>


		
