
Open forwards & redirects
-------

**Example:**

   	<?php
	
	/*
	When using forwards & redirects you should make sure the URL is being explicitly 
	declared in the code and cannot be manipulated by an attacker like:
	*/
	
	header("location:redirectpage.php");
	
	/*
	Generally you should avoid getting input into the redirect which could contain
	user-input by any means. if for any reason this may not be feasible than you 
	should make a whitelist input validation for the redirect like so:
	*/
	
	     
     
	//First we create a function which checks te allowed patterns
	function checkpattern(){
		$array = array("/^page1$/" ,"/^page2$/" ,"/^etc$/" ,"/^etc$/");
	
		foreach($array as $Pattern){
			while(preg_match($Pattern , $_GET['fileName'])){		
				//If the value is valid we send a log to the logging file.        
				setLog($_SESSION['userID'],"Validation was succesfull for filename", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL"); 
				
				//if valid than we redirect the user towards the new page
				header("location:index.php?succes=$_GET['filename']");
				
				//then we return true      			
				return true;
			}

		}
	}
	
	//Here we handle the consequences if the checkpattern function fails
	if(checkpattern() !== true){
		
		//Set a log for whenever there is unexpected user input with a threat level:
		setLog($_SESSION['userID'],"Detection of malicous input in file include", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");
		
		/*
		If the user tries to redirect to other pages than specified, immediate logout wil follow!
		*/
		setCounter(3);
					
		//The die function is to make sure the rest of the php code is not excecuted beyond this point
		die(); 
	}
	
	?>