# Character encoding
-------

## Example:


    <?php

	/*
	This is the encoder class for whenever you have to allow certain
	possibly dangerous characters into your code for i.e names such as O'Reilly
	*/

	class encodeInput {
		//As you can see you can specify allowed characters in your function
		public function encoder($allowed, $input, $countLevel){

			//create object for logging class
			$logging = new logging();

			$return = true;

			if(!preg_match("/^[a-zA-Z0-9 ".$allowed."]+$/", $input)){		

				/*
				Set a log for whenever there is unexpected user input with a threat level
				See "audit logs" code example for more information:
				*/
				$logging->setLog($_SESSION['userID'],"Bad user inputs", "FAIL",
				date("d-m-y"), $_SESSION["privilege"], "HIGH");

				/*
				Set counter if counter hits 3 the users session must terminated
				After 3 session terminations the user account must be blocked
				See "audit logs" code example for more information:
				*/			
				$logging->setCounter($countLevel);
				$input = false;
			}

			//We also check for the single quote since htmlspecialchar does not encode it
			if(preg_match("/'/", $input)){
				$input = preg_replace("/'/", "&#39;", $input);
			}

			//We return the input by means of htmlspecialcharacters so it becomes encoded
			return htmlspecialchars($input);
		}
	}//end class

    ?>
