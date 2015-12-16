
X-path query
-------

**Example:**



    	<?php

		//start a new domdocument

        $xmldoc = new DOMDocument();
        $xmldoc->load('test.xml');

        $xpathvar = new Domxpath($xmldoc);

		//define break out patterns
		
		$pattern1 = "/'/";

		/* possible sanitizer patterns. In this case we want to use people's names so we also have
		want to allow input like: o'reily.
		*/

		$pattern2  ='/^[a-zA-Z0-9]+&apos;?[a-zA-Z0-9]+$/D';
		$pattern3  ='/^[a-zA-Z0-9]/';
				
		/*
		disarm the brake-out userinput by replacing ' with &apos;
		*/		
		$replacements = "&apos;";
		$string = $_POST['search'];
		
	
		//First we check if only the intended values where posted by the user		
		while(!preg_match($pattern2 , $string) || preg_match($pattern3, $string)){

        	//Set a log for whenever there is unexpected userinput with a threat level
			setLog($_SESSION['userID'],"Unintended post value", "FAIL", date(dd-mm-yyyy), $privelige, "MOD");
        
            /*
			Set counter if counter hits 3 the users session must terminated
			After 3 session terminations the user acount must be blocked
			*/
			setCounter(1);
		       
		}

			
		/*
		Verify the sanitizer pattern. In this case we want to use people's names so we also have
		want to allow input like: o'reily.
		*/
		$array = array($pattern1);
		
		foreach($array as $pattern){	
			while(preg_match($pattern , $string)){
				$result = preg_replace($pattern1, $replacements, $string);
			}		
		}
		
		
		/*
		After succesfully sanitizing the userinput we want to execute the x-path query 
		First we log the succesfull validation
		*/
		
		setLog($_SESSION['userID'],"Succesfull userinput validation for X-Path", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL");
		if(preg_match($pattern2, $result) || preg_match($pattern3, $result)) :
		
        $queryResult = $xpathvar->query('//lemonade[@supplier="'.$result.'"]/price');
        
        foreach($queryResult as $result){
                echo $result->textContent;
        }		
		
		endif;
		
	?>


	