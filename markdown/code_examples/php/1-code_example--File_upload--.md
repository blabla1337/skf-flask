
File upload
-------

**Example:**


    <?php

	function Image()
	
		{
			//File location ouside of the root
			$uploaddir = 'assets/uploads/';

			//if smaller than zero it's no file	
			if(getimagesize($this->_image['tmp_name']) < 0)
			{
		
				//Set counter if counter hits 3 the users session must terminated
				//After 3 session terminations the user acount should be blocked
				setCounter(1);
			
				//Set a log for whenever there is unexpected userinput with a threat level
				setLog($_SESSION['userID'],"No valid image", "FAIL", date(dd-mm-yyyy), $privelige, "MOD");
			
				header('location:/page');
			
				die;
			}
		
			//Check for mime type of the file
			if($this->_image['type'] != 'image/png' && $this->_image['type'] != 'image/jpeg') 
			{	

				/*
				Set counter if counter hits 3 the users session must terminated
				After 3 session terminations the user acount must be blocked
				Since the high threat level there will be imediate session termination
				*/
				setCounter(3);
			
				//Set a log for whenever there is unexpected userinput with a threat level
				setLog($_SESSION['userID'],"invalid image mime type", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");
			
				header('location:/page');
			
				die;
			}
				
			//check extensions
			$filetype 	   = explode(".", $this->_image['name']);
			$takeLastValue = count($filetype) - 1;			
		
				while( ($filetype[$takeLastValue] != "png") && ($filetype[$takeLastValue] != "jpg"))
				{	
			
				/*
				Set counter if counter hits 3 the users session must terminated
				After 3 session terminations the user acount should be blocked
				Since the high threat level there will be imediate session termination
				*/
				setCounter(3);
			
				//Set a log for whenever there is unexpected userinput with a threat level
				setLog($_SESSION['userID'],"Unrestrected image extension upload", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");
				
					die;
				}
		
			//Check for uploading out of intended directory
			$array = array("/%2e%2e%2f/" ,"/..//" ,"/%2e/" ,"/%5c/" ,"/%252e/" ,"/%c0%af/" ,"%/c1%9c/");
		
			foreach($array as $injectPattern)
			{
				while(preg_match($injectPattern , $this->_image['name']))
				{
			
					/*
					Set counter if counter hits 3 the users session must terminated
					After 3 session terminations the user acount should be blocked
					Since the high threat level there will be imediate session termination
					*/
					setCounter(3);
			
					//Set a log for whenever there is unexpected userinput with a threat level
					setLog($_SESSION['userID'],"Unrestricted image filename", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");
				
					die;
				}		
			}
			
			//if all goes wel upload your file	
		
			$uploadfile = $uploaddir . basename($this->_image['name']);
			move_uploaded_file($this->_image['tmp_name'], $uploadfile);	
		
			//Last mime type check after upload if not correct than delete!
			$finfo = finfo_open(FILEINFO_MIME_TYPE);
			echo $theType = finfo_file($finfo, $uploaddir.$this->_image['name']);
		
				if($theType != "image/jpeg" && $theType != "image/png")
				{	
					unlink($uploaddir.$this->_image['name']);
								/*
					Set counter if counter hits 3 the users session must terminated
					After 3 session terminations the user acount should be blocked
					Since the high threat level there will be imediate session termination
					*/
					setCounter(3);
			
					//Set a log for whenever there is unexpected userinput with a threat level
					setLog($_SESSION['userID'],"invalid image mime type", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");
				
					die;
				
				}

		}
	?>


	