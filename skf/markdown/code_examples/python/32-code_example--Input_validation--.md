
input validation
-------

**Example:**
   

    <?php
       
        /*
     	First example is about input validation. We want to filter the user input for expected values, 
     	for this example we only expect a-z/0-9. Whenever the values are tampered with
        we can assume a hacker is trying to inject malicious input
     	*/
     	
     	if(!preg_match("/^[a-zA-Z0-9]+$/", $_POST['userinput']))
     	{
     		//Set a log for whenever there is unexpected userinput with a threat level
			setLog($_SESSION['userID'],"invalid expected input", "FAIL", date(dd-mm-yyyy), $privelige, "MOD");
     	
     		/*
			Set counter if counter hits 3 the users session must terminated
			After 3 session terminations the user acount must be blocked
			*/
			setCounter(1);
     	}
     
     
        /*
        Seccond example, let's assume you have a checkbox form on your application, whenever a checkbox is checked it has a certain
        fixed expected value. whenever these value's differ from your fixed value's you can determin the user is tampering
        the value's and should be blocked since he is probably intercepting your parameters with an intercepting proxy. 
        */
	
	//First we create a function which checks te allowed patterns
	function checkpattern(){
		$array = array("/^page1$/" ,"/^page2$/" ,"/^etc$/" ,"/^etc$/");
	
		foreach($array as $Pattern){
			while(preg_match($Pattern , $_GET['fileName'])){		
				//If the value is valid we send a log to the logging file.        
				setLog($_SESSION['userID'],"Validation was succesfull for filename", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL"); 
			
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
		If the user tries to read files other than specified, immediate logout wil follow!
		*/
		setCounter(3);
					
		//The die function is to make sure the rest of the php code is not excecuted beyond this point
		die(); 
	}
	
        
        /*
        Third example is an encoding routine where we take possible malicious input and transform it into harmless input.
        */
        
        //define break out pattern for encoding
		$pattern1 = "/'/";

		/* 
		possible sanitizer patterns. In this case we want to use people's names so we also have
		want to allow input like: o'reily.
		*/

		$pattern2  ='/^[a-zA-Z0-9]+&apos;?[a-zA-Z0-9]+$/D';
		$pattern3  ='/^[a-zA-Z0-9]/';
				
		/*
		disarm the brake-out userinput by replacing ' with &apos;
		*/		
		$replacements = "&apos;";
		$string = $_POST['username'];
		
		
		/*
		Verify the sanitizer pattern. In this case we want to use people's names so we also have
		want to allow input like: o'reily. 
		Don't forget to sanitise all other evil input first before allowing the user-input 
		to process any further. you can achieve this by using the same type of check as used
		in the first example, exept we use another regex like:
		
		/^['a-zA-Z0-9]+$/
		
		*/
		$array = array($pattern1);
		
			foreach($array as $pattern)
			{	
				while(preg_match($pattern , $string))
				{
					setLog($_SESSION['userID'],"character encoding for username", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL");
					$result = preg_replace($pattern1, $replacements, $string);	
					return true;				
				}		
			}
		
		
		//Another example for character encoding would be: 
		
		//POST value harmfull state:
		$vulnerable = $_POST['value'];
		echo $vulnarable

		//POST value escaped state:
		$escaped = htmlspecialchars($_POST['value']);
		echo $escaped;
		
		/*
		By putting the POST value in the htmlspecialchars() function all malicious userinput such as:
		< / > '"& etc will me encoded into harmless formats.
		*/
        
    ?>