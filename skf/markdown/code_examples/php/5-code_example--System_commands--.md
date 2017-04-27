
	
System commands
-------

**Example:**

    <?php

	class systemCommands{ 	

		/*
		Define the whitelist pattern and validation type and input parameter like:
		getFiles("value1,value2,etc", "alphanummeric", $_GET['filename'], "3")
		*/
		public function command($whiteListPattern, $validationType, $inputParameter){
		
			//Here we include all the necessary classes like audit logs, whitelisting and validation:
			include("classes.php");
			
			$validate  = new validation();
			$whitelist = new whitelisting();
	
			$continue = true;
		
			/*
			Whenever a system command is finished, you should properly sanitise and escape this user input.
			System command functions examples are: system(), eval(), exec()
		
			First, we want to filter the filenames for expected values. For this example we use only a-z/0-9
			Whenever the values are tampered with, we can assume an attacker is trying to inject malicious input.
			for more information about validation see "input validations" in the code examples:
			*/
		
			if($validate->inputValidation($inputParameter, $validationType, 
			"Invalid userinput for system commands", "HIGH", $countLevel) == false) {$continue = false;}
 
			/*
			Seccond, we want to whitelist the filenames for expected values, in this example they are,
			page1,page2 etc.. for more information about whitelisting see "white-listing" in the code examples:
			*/
		
			if($whitelist->checkpattern($whiteListPattern, $inputParameter, $countLevel) == false)
			{$continue = false;}

			//If all went good we include the filename
			if($continue == true){
					
				//Even though there is a match we still escape the shellcommand:
				$command = './configure '.$inputParameter;
				$escaped_command = escapeshellcmd($command); 
				//Only after validation do we put the shellcommand into the system() function:
				system($inputParameter); 
			}
		}
	}
	
    ?>


	
		