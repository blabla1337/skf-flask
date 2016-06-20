
File upload
-------

**Example:**



    <?php
    
    
    //here we create a function which checks te allowed patterns
	function checkpattern(){
		    
		    //Check for uploading out of intended directory
			$array = array("/%2e%2e%2f/" ,"/..//" ,"/%2e/" ,"/%5c/" ,"/%252e/" ,"/%c0%af/" ,"%/c1%9c/");
	
				foreach($array as $Pattern){
					while(preg_match($Pattern , $this->_image['name'])){		
						//If the value is valid we send a log to the logging file.        
						setLog($_SESSION['userID'],"Validation was succesfull for filename", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL"); 
			
						//then we return true      			
						return true;
					}

				}
			}
    

	function Image(){

			//File location ouside of the root
			$uploaddir = 'assets/uploads/';

			//if smaller than zero it's no file	
			if(getimagesize($this->_image['tmp_name']) < 0){
		
				//Set a log for whenever there is unexpected userinput with a threat level
				setLog($_SESSION['userID'],"No valid image", "FAIL", date(dd-mm-yyyy), $privelige, "MOD");

		
				//Set counter; if counter hits 3, the user's session must be terminated.
				//After 3 session terminations the user acount should be blocked
				setCounter(1);
						
				header('location: /page');
				//The die function is to make sure the rest of the php code is not excecuted beyond this point
				die();
			}
		
			//Check for mime type of the file
			if($this->_image['type'] != 'image/png' && $this->_image['type'] != 'image/jpeg'){	

				//Set a log for whenever there is unexpected userinput with a threat level
				setLog($_SESSION['userID'],"invalid image mime type", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");

				/*
				Set counter; if counter hits 3, the user's session must be terminated.
				After 3 session terminations the user acount must be blocked
				Since the high threat level there will be imediate session termination
				*/
				setCounter(3);
						
				header('location:/page');
			
				//The die function is to make sure the rest of the php code is not excecuted beyond this point
				die();
			}
				
			//check extensions
			$filetype 	   = explode(".", $this->_image['name']);
			$takeLastValue = count($filetype) - 1;			
		
				while( ($filetype[$takeLastValue] != "png") && ($filetype[$takeLastValue] != "jpg")){	
			
					//Set a log for whenever there is unexpected userinput with a threat level
					setLog($_SESSION['userID'],"Unrestrected image extension upload", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");
			
					/*
					Set counter; if counter hits 3, the user's session must be terminated.
					After 3 session terminations the user acount should be blocked
					Since the high threat level there will be imediate session termination
					*/
					setCounter(3);
								
					//The die function is to make sure the rest of the php code is not excecuted beyond this point
					die();
				}
		
			
	
			//Here we handle the consequences if the checkpattern function fails as restricted in the checkpattern function
			if(checkpattern() !== true){
		
				//Set a log for whenever there is unexpected user input with a threat level:
				setLog($_SESSION['userID'],"Detection of malicous input in file include", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");
		
				/*
				If the user tries to read files other than specified, immediate logout wil follow!
				*/
				setCounter(3);
					
				//The die function is to make sure the rest of the php code is not excecuted beyond this point
				die(); 
			}
	
			
			//if all goes wel upload your file, first we want to log the event.	
			setLog($_SESSION['userID'],"File upload", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL");
			$uploadfile = $uploaddir . basename($this->_image['name']);
			move_uploaded_file($this->_image['tmp_name'], $uploadfile);	
		
			//Last mime type check after upload if not correct than delete!
			$finfo = finfo_open(FILEINFO_MIME_TYPE);
			echo $theType = finfo_file($finfo, $uploaddir.$this->_image['name']);
		
				if($theType != "image/jpeg" && $theType != "image/png"){	
					unlink($uploaddir.$this->_image['name']);
		
					//Set a log for whenever there is unexpected userinput with a threat level
					setLog($_SESSION['userID'],"invalid image mime type", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");
		
					/*
					Set counter; if counter hits 3, the user's session must be terminated.
					After 3 session terminations the user acount should be blocked
					Since the high threat level there will be imediate session termination
					*/
					setCounter(3);
					
					//The die function is to make sure the rest of the php code is not excecuted beyond this point
					die();				
				}

		}
	?>


	
