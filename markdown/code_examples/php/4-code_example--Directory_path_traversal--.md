
Directory/path traversal
-------

**Example:**



         	<?php
     
     	//First we want to filter the filenames for expected values, for this example we use only a-z/0-9
     	//Whenever the values are tampered with we can assume a hacker is trying to inject malicious input
     	if(!preg_match("/^[a-zA-Z0-9]+$/", $_GET['fileName'])
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
     
     
        //The seccond layer is to define the allowed pages to be read by the user
        $array = array("/page1/" ,"/page2/" ,"/etc/" ,"/etc/");
        
        foreach($array as $injectPattern)
        {
            while(!preg_match($injectPattern , $_GET['fileName']]))
            {
            
            /*
			If the user tries to read other files than specified, imediate logout wil follow!
			*/
			setCounter(3);
			
			//Set a log for whenever there is unexpected userinput with a threat level
			setLog($_SESSION['userID'],"Detection of malicous input in file include", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");
            die;
            
            }        
        }
     
        //Check for path traversal patterns
        $array = array("/%2e%2e%2f/" ,"/..//" ,"/%2e/" ,"/%5c/" ,"/%252e/" ,"/%c0%af/" ,"%/c1%9c/");
        
        foreach($array as $injectPattern)
        {
            while(preg_match($injectPattern , $_GET['fileName']))
            {
            
            /*
			The same goes for path traversal patterns, imediate logout!
			*/
			setCounter(3);
			
			//Set a log for whenever there is unexpected userinput with a threat level
			setLog($_SESSION['userID'],"Detection of malicous input in file include", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");
            die;
            
            }        
        }
        
        
		//ready for include
        include($_GET['fileName']);
        
        ?>


	