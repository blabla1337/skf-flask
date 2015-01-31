
System commands
-------

**Example:**



				/*
		whenever a system command is done you should properly sanitise and escape this userinput.
		system command functions could be:
		system()
		eval()
		exec()
		etc:
		*/


		$whiteList = "/allowed argument/";

		$sanitised = preg_match($whiteList, $_POST['configure_options'], $matched);

			if($matched)
			{
				$command = './configure '.$sanitised;
				$escaped_command = escapeshellcmd($command); 
				system($escaped_command); 
			}else{
				die;
			 }




	