
File upload
-------

**Example:**



		   

		function Image()
	
			{
				//File location ouside of the root
			$uploaddir = 'assets/uploads/';

			//if smaller than zero it's no file	
			if(getimagesize($this->_image['tmp_name']) < 0)
			{
				header('location:/login');
				die;
			}
		
			//Check for mime type of the file
			if($this->_image['type'] != 'image/png' && $this->_image['type'] != 'image/jpeg') 
			{	
				header('location:/login');
				die;
			}
				
			//check extensions
			$filetype 	   = explode(".", $this->_image['name']);
			$takeLastValue = count($filetype) - 1;			
		
				while( ($filetype[$takeLastValue] != "png") && ($filetype[$takeLastValue] != "jpg"))
				{	
					header('location:/login');
					die;
				}
		
			//Check for uploading out of intended directory
			$array = array("/%2e%2e%2f/" ,"/..//" ,"/%2e/" ,"/%5c/" ,"/%252e/" ,"/%c0%af/" ,"%/c1%9c/");
		
			foreach($array as $injectPattern)
			{
				while(preg_match($injectPattern , $this->_image['name']))
				{
					header('location:/login');
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
					header('location:/login');
					die;
				}

		}
    


	