X-path query
-------

**Example:**

    <?php
    
	class xPathControll{ 	

		/*
		Define the allowed characters and input parameter and countlevel for the 
		user lockout like:
		controller("<'>&", $_GET['filename'], "3")
		*/
		public function controller($allowedCharacters, $inputParameter, $countLevel){
			
			//Include the classes where you want to make objects of:		
			include("classes.php");
			$encode = new encodeInput();

			/* 
			First we build our encoding method, see "input validation" code example for
			more detailed information about encoding and escaping.
			*/
	
			$return = $encode->encoder($allowedCharacters, $inputParameter, $countLevel);
			
			//If the encoder came back false we do not proccess the function!
			if($return !== false){
				//start a new domdocument

				$xmldoc = new DOMDocument();
				$xmldoc->load('test.xml');

				$xpathvar = new Domxpath($xmldoc);

				/*
				Assuming that you used the encoder function also for adding users, it will now retreive the
				user o'reily from the query
				*/
	
				$queryResult = $xpathvar->query('//lemonade[@supplier="'.$return.'"]/price');
	
				foreach($queryResult as $result){
						echo $result->textContent;
				}
			}
		}
	}
        ?>


	
			
	