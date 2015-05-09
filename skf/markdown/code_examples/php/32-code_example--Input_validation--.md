
input validation
-------

**Example:**
   

    <?php
    
	class inputvalidation {

		/*
		First example is about input validation. We want to filter the user input for expected values.
		Whenever the values are tampered with we can assume a hacker is trying to inject malicious input
		*/
	
		public function validate($input, $type, $logMessage, $threatLevel){
	
		switch ($type) {
			case "nummeric":
				$pattern = "/^[0-9]+$/";
				break;
			case "alphanummeric":
				$pattern = "/^[a-zA-Z0-9]+$/";
				break;
		}

		if(!preg_match($pattern, $input)){

			//Set a log for whenever there is unexpected userinput with a threat level
			setLog($_SESSION['userID'], $logMessage, "FAIL", date(dd-mm-yyyy), $privelige, $threatLevel);

			/*
			Set counter if counter hits 3 the users session must terminated
			After 3 session terminations the user acount must be blocked
			*/			
			setCounter(1);
	
			//The die function is to make sure the rest of the php code is not excecuted beyond this point
			return false;
		}else{
		
			//Set a log for whenever there is unexpected userinput with a threat level
			setLog($_SESSION['userID'],"Valid input validation for regex from", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL");
			echo "was true";
			return true;
			}
		 }
		 
		 
		/*
		Seccond example, let's assume you have a checkbox form on your application, whenever a checkbox is checked it has a certain
		fixed expected value. whenever these value's differ from your fixed value's you can determin the user is tampering
		the value's and should be blocked since he is probably intercepting your parameters with an intercepting proxy. 
		*/
	
	
		//First we create a function which checks te allowed patterns
		public function checkpattern(){
			$array = array("/^page1$/" ,"/^page2$/" ,"/^etc$/" ,"/^etc$/");
	
			foreach($array as $Pattern){
				while(preg_match($Pattern , $_GET['fileName'])){		
					//If the value is valid we send a log to the logging file.        
					setLog($_SESSION['userID'],"Validation was succesfull for filename", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL"); 
			
					//Whenever there was a valid match we return true      			
					return true;
				}

			}
		}
	
	
		/*
		Last but not least is an encoder functionality for whenever you have to allow certain
		possibly dangerous characters into your code for i.e names such as o'reily
		*/
	
		//As you can see you can specify allowed characters in your function
		public function encoder($input, $allowed){
		
		if(!preg_match("/^[a-zA-Z0-9 ".$allowed."]+$/", $input)){		
		
			//Set a log for whenever there is unexpected userinput with a threat level
			setLog($_SESSION['userID'], $logMessage, "FAIL", date(dd-mm-yyyy), $privelige, $threatLevel);

			/*
			Set counter if counter hits 3 the users session must terminated
			After 3 session terminations the user acount must be blocked
			*/			
			setCounter(1);
			$input = "Error";			
		}
		
		//We also check for the single qoute since htmlspecialchar does not encode it
		if(preg_match("/'/", $input)){
			$input = preg_replace("/'/", "&#39;", $input); 
		}
	
	
		//We return the input by means of htmlspecialcharacters so it becomes encoded
		return htmlspecialchars($input);
	}

	/*
	Now let's talk about the usages of al three examples above:
	*/
	
	$inputvalidation = new inputvalidation();
	
	/*
	First example.
	Whenever calling on this function for by example nummeric validation 
	you have to use it as follows:
	*/
	
	if($inputvalidation->validate($input, "nummeric", "Log message for failure", "theatlevel")!== true){ /* DO SOMETHING */} 
	
	/*
	Seccond example.
	Whenever calling on the seccond example you can use it as follows:
	*/
	
	//Here we handle the consequences if the checkpattern function fails
	if($inputvalidation->checkpattern() !== true){
	
		//Set a log for whenever there is unexpected user input with a threat level:
		setLog($_SESSION['userID'],"Detection of malicous input in file include", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");
	
		/*
		If the user tries to read files other than specified, immediate logout wil follow!
		*/
		setCounter(3);
				
		//The die function is to make sure the rest of the php code is not excecuted beyond this point
		die(); 
	}
		
		/*
		Third example is an encoding routine where we take possible malicious input and transform it into harmless input.
		*/
		
		//For the sake of example we want to allow the user to use an '&' as input: 
		$encoded =  $inputvalidation->encoder($userinput, "&");
	
	}       
    ?>