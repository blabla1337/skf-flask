 
White-listing
-------

**Example:**
   
       <?php

    
	class whitelisting extends logging {
		/*
		First we create a function which checks te allowed patterns:
		checkpattern("value1,value2,value3" , $input, "3")
		*/
		 function checkpattern($allowed, $input, $countLevel){
			
    		$logging = new logging();
    		$result  = explode("," , $allowed);
			
			$results = false;
			
			foreach($result as $pattern){
				while(preg_match("/^".$pattern."$/", $input)){		
					//If the value is valid we send a log to the logging file.        
					$logging->setLog($_SESSION['userID'],"Good whitelist validation", "SUCCESS", date("d-m-y"), $_SESSION["privilege"], "HIGH"); 
			
					$results = true;
					
					//Whenever there was a valid match we return true      			
					return true;
				}
			}
			//Check for a false in order to send error to log and counter the user.
			if($results == false){
				//If the value is invalid we send a log to the logging file.        
				$logging->setLog($_SESSION['userID'],"Bad whitelist validation", "FAIL", date("d-m-y"), $_SESSION["privilege"], "HIGH"); 
				//$logging->setCounter($countLevel);			
			}
		}
	}//end class
	
    ?>