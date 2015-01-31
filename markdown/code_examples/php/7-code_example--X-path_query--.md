
X-path query
-------

**Example:**



				//start a new domdocument

        $xmldoc = new DOMDocument();
        $xmldoc->load('test.xml');

        $xpathvar = new Domxpath($xmldoc);

		//define break out patterns
		
		$pattern1 = "/'/";
		$pattern0 = '/"/';

		/* possible sanitizer patterns. In this case we want to use people's names so we also have
		want to allow input like: o'reily.
		*/

		$pattern2  ='/^[a-zA-Z0-9]+&apos;?[a-zA-Z0-9]+$/D';
		$pattern3  ='/^[a-zA-Z0-9]/';
				
		/*
		disarm the brake-out userinput by replacing ' with &apos;
		*/		
		$replacements = "&apos;";
		$string = $_POST['search'];
		
	
		//Check for uploading out of intended directory
		$array = array($pattern0 , $pattern1);
		
		foreach($array as $pattern)
		{
			while(preg_match($pattern , $string))
			{
				$result = preg_replace($pattern0, $replacements, $string);
			}
			
			while(preg_match($pattern , $string))
			{
				$result = preg_replace($pattern1, $replacements, $string);
			}		
		}
		
		
		/*
		After succesfully sanitizing the userinput we want to execute the x-path query 
		*/
		
		if(preg_match($pattern2, $result) || preg_match($pattern3, $result)) :
		
        $queryResult = $xpathvar->query('//lemonade[@supplier="'.$result.'"]/price');
        foreach($queryResult as $result){
                echo $result->textContent;
        }		
		
		endif;
		
	?>


	