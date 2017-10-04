# File upload
-------

## Example:


	<?php

	class fileUpload{
		
		public function Image(){

			include('classes.php');
			$validated = new validate();
			$log = new logging();


			$image = $_FILES['fileToUpload'];
			//File location outside of the root
			$uploaddir = 'assets/uploads/';

			//check extensions
			$filetype = explode(".", $image['name']);

			/*
			For uploading out of intended directory we check the filename and verify that it only contains alphanumeric values.
			*/
			if($validated -> inputValidation($filetype[0], "alphanumeric", "invalid filename", "MOD", 2){
				header('location:/page');
				die();
			}

			/*
			We take the last array value to make sure it is the last extension to prevent validating
			.jpg.php in a file name.
			*/
			$takeLastValue = count($filetype) - 1;

			while(($filetype[$takeLastValue] != "png") && ($filetype[$takeLastValue] != "jpg")){

				//Set a log for whenever there is an unexpected user input with a threat level
				$log -> setLog($_SESSION['userID'],"Unrestricted image extension upload",
				"FAIL", date(dd-mm-yyyy), $privilege, "HIGH");

				/*
				Set counter; if counter hits 3, the user's session must be terminated.
				After 3 session terminations the user account should be blocked
				Since the high threat level will lead to immediate session termination
				*/
				$log -> setCounter(3);

				//The die function is to make sure the rest of the php code is not executed beyond this point
				die();
			}

			 // Check file size
			if($image["size"] > 500000) {
				 header('location:/page');
				 die();
			 }

			// Check if file already exists to prevent overwriting
			if(file_exists('assets/uploads/'.$image['name'])) {
				header('location:/page');
				die();
			}  

			//if all goes well upload your file, first we want to log the event.
			$log -> setLog($_SESSION['userID'],"File upload", "SUCCESS", date(dd-mm-yyyy),
			$privilege, "NULL");

			$uploadfile = $uploaddir . basename($image['name']);
			move_uploaded_file($image['tmp_name'], $uploadfile);

			//Last mime type check after upload if not correct than delete!
			$finfo = finfo_open(FILEINFO_MIME_TYPE);
			echo $theType = finfo_file($finfo, $uploaddir.$image['name']);

			if($theType != "image/jpeg" && $theType != "image/png"){    
				unlink($uploaddir.$image['name']);

				//Set a log for whenever there is unexpected user input with a threat level
				$log -> setLog($_SESSION['userID'],"invalid image mime type",
				"FAIL", date(dd-mm-yyyy), $privilege, "HIGH");

				/* ^^
				Set counter; if counter hits 3, the user's session must be terminated.
				After 3 session terminations the user account should be blocked
				since the high threat level can lead to immediate session termination.
				*/
				$log -> setCounter(3);

				//The die function is to make sure the rest of the php code is not executed beyond this point
				die();              
			}
		}
	}
	?>
