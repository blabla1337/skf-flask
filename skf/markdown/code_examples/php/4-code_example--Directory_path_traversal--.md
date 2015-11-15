Directory/path traversal
-------

**Example:**

    <?php
    
	class fileGetContents{ 	
		/*
		Define the whitelist pattern and validation type and input parameter, countLevel like:
		getFiles("page1,page2,etc", "alphanummeric", $_GET['filename'], "3")
		*/
		public getFiles($whiteListPattern, $validationType, $inputParameter, $countLevel){
		
			//Include the classes of which you want to use objects from
			include_once("classes.php");
				
			$validate  = new validation();
			$whitelist = new whitelisting();
	
			$continue = true;
		
			/*
			First, we want to filter the filenames for expected values. For this example we use only a-z/0-9
			Whenever the values are tampered with, we can assume an attacker is trying to inject malicious input.
			for more information about validation see "input validations" in the code examples:
			*/
			if($validate->inputValidation($inputParameter, $validationType, 
			"Invalid userinput", "HIGH", $countLevel) == false) {$continue = false;}
	 
			/*
			Second, we want to whitelist the filenames for expected values, in this example they are,
			page1,page2 etc.. for more information about whitelisting see "white-listing" in the code examples:
			*/
			if($whitelist->checkpattern($whiteListPattern, $inputParameter, $countLevel) == false)
			{$continue = false;}
	
			//If all went good we include the filename
			if($continue == true){
				include($inputParameter);
			}
		} 
	}
    ?>


	
