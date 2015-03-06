
Single input validation
-------

**Example:**

    <?php
	
	/*
	This function is where you store al your input validation controls. 
	It makes it easy to maintain whenever you want to apply changes for 
	certain input validation roles and reduces the chance of mistakes in your regexes.
	*/
	
	
	//Here we expect only alphanumeric value's
	function singleInputValidationAlphaNumeric($input){
	
		if(!preg_match("/^[a-zA-Z0-9]+$/", $input){
		
			//Set a log for whenever there is unexpected userinput with a threat level
			setLog($_SESSION['userID'],"invalid expected input Alphanumeric", "FAIL", date(dd-mm-yyyy), $privelige, "MOD");
	
			/*
			Set counter if counter hits 3 the users session must terminated
			After 3 session terminations the user acount must be blocked
			*/			
			setCounter(1);
			
			//The die function is to make sure the rest of the php code is not excecuted beyond this point
			die;
			
		}else{
			//Set a log for whenever there is unexpected userinput with a threat level
			setLog($_SESSION['userID'],"Valid input validation for Alphanumeric", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL");
			return true;
		}
     }
    
     
     /*
     This is how we would apply our functions into our code.
	 Let's say we would expect only an numeric value in this example, than we would use the 
	 singleInputValidationNumeric function like this
	 */
	 
	 if(singleInputValidationNumeric($_POST['number']) == true);
	 
     
	?>