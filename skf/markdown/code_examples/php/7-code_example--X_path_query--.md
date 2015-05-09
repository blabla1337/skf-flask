
X-path query
-------

**Example:**


    <?php
	
	/* 
	First we build our encoding method, see "input validation" code example for
	more detailed information about encoding and escaping.
	*/
	
	function encoder($input, $allowed){
    	
		if(!preg_match("/^[a-zA-Z0-9 ".$allowed."]+$/", $input)){		

			//Set a log for whenever there is unexpected userinput with a threat level
			//setLog($_SESSION['userID'], $logMessage, "FAIL", date(dd-mm-yyyy), $privelige, $threatLevel);

			/*
			Set counter if counter hits 3 the users session must terminated
			After 3 session terminations the user acount must be blocked
			*/			
			setCounter(3);
			die();			
		}
		
		//htmlspeciarchars does not ecode ' so we do it manualy
		if(preg_match("/'/", $input)){
			$input = preg_replace("/'/", "&#39;", $input); 
		}
	
		return htmlspecialchars($input);
	}
	
	//start a new domdocument

	$xmldoc = new DOMDocument();
	$xmldoc->load('test.xml');

	$xpathvar = new Domxpath($xmldoc);

	/*
	After succesfully sanitizing the userinput we want to execute the x-path query 
	First we log the succesfull validation
	*/
	
	//First we define the ' as a allowed character
	$allowed = "'";    
	
	/*
	We set the input manualy to o'reily for the example every special character that does
	not comply with allowed generates an error and lockout
	*/
	$bar =  encoder("o'reily", $allowed);

	//before doing anyting with our x-path we log the valid input validation
	setLog($_SESSION['userID'],"Succesfull userinput validation for X-Path", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL");
	
	/*
	Assuming that you used the encoder function also for adding users, it will now retreive the
	user o'reily from the query
	*/
	
	$queryResult = $xpathvar->query('//lemonade[@supplier="'.$result.'"]/price');
	
	foreach($queryResult as $result){
			echo $result->textContent;
	}		
	
		
	?>


	