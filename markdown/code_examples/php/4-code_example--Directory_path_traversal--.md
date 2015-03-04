
Directory/path traversal
-------

**Example:**



        <?php
     
     	//First, we want to filter the filenames for expected values. For this example we use only a-z/0-9
     	//Whenever the values are tampered with, we can assume an attacker is trying to inject malicious input.
     	if(!preg_match("/^[a-zA-Z0-9]+$/", $_GET['fileName']){

     		/*
			Set counter; if counter hits 3, the user's session must be terminated.
			After 3 session terminations the user's acount must be blocked.
			Given the high threat level, there will be immediate session termination.
			*/
			setCounter(3);
			
			//Set a log for whenever there is unexpected userinput with a threat level
			setLog($_SESSION['userID'],"invalid expected input", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");
     	}
     
     
        //The seccond layer is to define the allowed pages to be read by the user
        $array = array("/page1/" ,"/page2/" ,"/etc/" ,"/etc/");
        
        foreach($array as $injectPattern){
            while(!preg_match($injectPattern , $_GET['fileName']])){
            
            /*
			If the user tries to read files other than specified, immediate logout wil follow!

			*/
			setCounter(3);
			
			//Set a log for whenever there is unexpected user input with a threat level:
			setLog($_SESSION['userID'],"Detection of malicous input in file include", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");
            //The die function is to make shure the rest of the php code is not excecuted beyond this point
            die();            }        
        }
     
        //Check for path traversal patterns
        $array = array("/%2e%2e%2f/" ,"/..//" ,"/%2e/" ,"/%5c/" ,"/%252e/" ,"/%c0%af/" ,"%/c1%9c/");
        
        foreach($array as $injectPattern){
            while(preg_match($injectPattern , $_GET['fileName'])){
            
            /*
			The same goes for path traversal patterns, immediate logout!
			*/
			setCounter(3);
			
			//Set a log for whenever there is unexpected user input with a threat level
			setLog($_SESSION['userID'],"Detection of malicous input in file include", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");
            
            //The die function is to make shure the rest of the php code is not excecuted beyond this point
            die();             }        
        }
        
        
		//ready for include
        include($_GET['fileName']);
        
        ?>


	
