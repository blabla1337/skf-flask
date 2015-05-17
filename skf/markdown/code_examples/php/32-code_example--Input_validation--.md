
input validation
-------

**Example:**

  
   
    <?php
	
	/*
	This function is where you store al your input validation controls. 
	It makes it easy to maintain whenever you want to apply changes for 
	certain input validation roles and reduces the chance of mistakes in your regexes.	
	*/
     	
	class validation{
		 
		//Our input validation function
		public function inputValidation($input, $type, $logMessage, $threatLevel, $countLevel){
			
			//Audit log and user lockdown 
			$logging = new logging();
				
			switch ($type) {
				case "nummeric":
					$pattern = "/^[0-9]+$/";
					break;
				case "alphanummeric":
					$pattern = "/^[a-zA-Z0-9]+$/";
					break;
			}
	
			if(!preg_match($pattern, $input)){
	
				/*
				Set a log for whenever there is unexpected userinput with a threat level
				See "audit logs" code example for more information:
				*/
				$logging -> setLog($_SESSION['userID'], $logMessage, "FAIL", date("d-m-y"), $_SESSION["privilege"], $threatLevel);

				/*
				Set counter if counter hits 3 the users session must terminated
				After 3 session terminations the user acount must be blocked
				See "audit logs" code example for more information:
				*/			
				//$logging->setCounter($countLevel);
			
				return false;
			}else{
					//Set a log for whenever there is unexpected userinput with a threat level
					$logging->setLog($_SESSION['userID'],"Valid input validation for regex from ".$type." ", "SUCCESS", date("d-m-y"), $_SESSION["privilege"], "NONE");
			
					return true;
			}  
		}
	}
    	     
	?>