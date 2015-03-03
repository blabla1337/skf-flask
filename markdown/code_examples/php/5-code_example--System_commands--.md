
System commands
-------

**Example:**



    	<?php

	/*
	whenever a system command is done you should properly sanitise and escape this userinput.
	system command functions could be:
	system()
	eval()
	exec()
	etc:
	*/

		 //First we want to filter the filenames for expected values, for this example we use only a-z/0-9
		 //Whenever the values are tampered with we can assume a hacker is trying to inject malicious input
		if(!preg_match("/^[a-zA-Z0-9]+$/", $_POST['configure_options'])
			{
				/*
				Set counter if counter hits 3 the users session must terminated
				After 3 session terminations the user acount must be blocked
				Since the high threat level there will be imediate session termination.
				*/
				setCounter(3);
		
				//Set a log for whenever there is unexpected userinput with a threat level
				setLog($_SESSION['userID'],"invalid expected input", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");
			}
 

	//Seccond we define the allowed arguments
	$whiteList = "/allowed argument/";

	//Next we validate the incoming userinput in a preg_match function
	$sanitised = preg_match($whiteList, $_POST['configure_options'], $matched);

		//if there is a match we can proceed 
		if($matched)
		{
			//even though there is a match we still escape the shellcommand
			$command = './configure '.$sanitised;
			$escaped_command = escapeshellcmd($command); 
	
			//Only after validation we put the shellcommand into the system() function
			system($escaped_command); 
		}else{		
				/*
				Set counter if counter hits 3 the users session must terminated
				After 3 session terminations the user acount must be blocked
				Since the high threat level there will be imediate session termination
				*/
				setCounter(3);
		
				//Set a log for whenever there is unexpected userinput with a threat level
				setLog($_SESSION['userID'],"Possible command injection attack on system function", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");        
				die(); 
		
			  }
		 }

	?>


	