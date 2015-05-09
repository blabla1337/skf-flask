
Single input validation
-------

**Example:**

    <?php
	
	/*
	This function is where you store al your input validation controls. 
	It makes it easy to maintain whenever you want to apply changes for 
	certain input validation roles and reduces the chance of mistakes in your regexes.
	
	See the "input validation" code example for the full complete function:
	*/
	
	//Our input validation function
	function inputValidation($input, $type, $logMessage, $threatLevel){
	
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
			//die;
			echo "was bad";
			return false;
		}else{
				//Set a log for whenever there is unexpected userinput with a threat level
				setLog($_SESSION['userID'],"Valid input validation for regex from", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL");
				echo "was true";
				return true;
			}
		 }
    
     
     /*
     This is how we would apply our functions into our code.
	 Let's say we would expect only an numeric value in this example, than we would use the 
	 singleInputValidationNumeric function like this
	 */
	 
	 if(inputValidation($_POST['input'], "nummeric", "Bad validation",  "HIGH") != true);
	 
     
	?>