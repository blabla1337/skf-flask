# Reflective file download and file download injection prevention
-------

## Example:

	<?php

	//include all necessary classes
	include_once("class/classCollect.php");

	class fileDownload{
		/*
		The first example we cover how to download files which users can upload
		themselves on the web application
		*/

		public function downloadUserFiles($fileID){		

			$conn = new NewDatabase();
			$db   = $conn -> connection();
			$validation = new validation();
			$proceed = true;

			/*
			For the sake of example we only allow the users to download their own files
			by identifier based sql query's. As you can see we select the filename
			by its id. in this case we prevent direct userinput into the disposition header.
			*/

			if($validation->inputValidation($fileID, "nummeric", "validate was false", "HIGH", 3) == false){
				$proceed = false;
			}

			if($proceed == true){
				$stmt = $db->prepare("SELECT * FROM download WHERE fileID=? AND userID=?");
				$stmt->execute(array($fileID, $_SESSION['userID']));
				$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);

				foreach($rows as $row){
					$filename = $row['fileName'];
					$mimeType = $row['mimeType'];
				}

				if($filename){
				/*
				We also define the mimetype per download file.
				This is because whenever a user can only download images it is not necessary to set
				an uncommon content-type header for it.
				NOTE: These mimetypes should not be stored based upon the mimetype which was send
				the reponse header when the user uploaded the file. This value can be easily
				manipulated with an intercepting proxy. You should get the mimetype from the file
				itself after it was stored on the server.
				*/
				header('Content-Description: File Transfer');
    			header("content-type:".$mimeType."");
    			header('Content-Disposition: attachment; filename='.$filename);
    			header('Expires: 0');
				header("Cache-Control: no-store, no-cache, must-revalidate, max-age=0");
				header("Cache-Control: post-check=0, pre-check=0", false);
				header("Pragma: no-cache");    
				header('Content-Length: ' . filesize($filename));
				//Last check to see if it really does exist.
				if(file_exists($filename)){
					readfile($filename);
				}
				/*
				Exit is very important, if other mechanims fail this makes sure the rest
				of the page plus attack string does not get downloaded anyways.
				*/
				exit;
				}
			}
		}

		/*
		The seccond example is for whenever you are providing users with fixed downloads
		such as manuals etc. We do not only check if the file just exists, because that would
		allow an attacker to also download important other files from your server, so instead
		we whitelist them.
		*/
		public function downloadStored($filename){

			$white = new whitelisting();

			if($white -> checkpattern("file1.txt,file2.txt", $filename, 3) != false){
				header('Content-Description: File Transfer');
    			header('Content-Type: text/plain');
    			header('Content-Disposition: attachment; filename='.$filename);
    			header('Expires: 0');
				header("Cache-Control: no-store, no-cache, must-revalidate, max-age=0");
				header("Cache-Control: post-check=0, pre-check=0", false);
				header("Pragma: no-cache");    
				header('Content-Length: ' . filesize($filename));
				if(file_exists($filename)){
					readfile($filename);
				}
				/*
				Exit is very important, if other mechanims fail this makes sure the rest
				of the page plus attack string does not get downloaded anyways.
				*/
				exit;
			}
		}
	}

	?>
