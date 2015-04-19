
XSL injection prevention
-------

**Example:**

   		
	/*
	In order to prevent XSL injections you must enforce strict policy's whenever the
	files are loaded from a source controlled by an possible attacker.
	
	Let's say for example that the user can choose from several XSL files on your application.
	
	ABC.xsl arranges your employee names on alphabetical order
	CBA.xsl does not care and just shows the input by order of your XML file.
	
	Before we want to attach the XSL files to the style sheet we first want to 
	do validation on the request to make sure the included file was one of our own pre
	defined files, like so:	
	*/

		//First we create a function which checks te allowed patterns
	function checkpattern(){
		$array = array("/^ABC.xsl$/" ,"/^CBA.xsl$/");

		foreach($array as $Pattern){
			while(preg_match($Pattern , $_GET['xsl'])){        
				
				//If the value is valid we send a log to the logging file.        
				setLog($_SESSION['userID'],"Validation was succesfull for filename", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL");

				//then we return true               
				return true;
			}

		}
	}

	//Here we handle the consequences if the checkpattern function fails
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

	# LOAD XML FILE
	// Load the XML source
	$xml = new DOMDocument;
	$xml->load('test.xml');

	$xsl = new DOMDocument('1.0','UTF-8');
	$xsl->load($_GET['xsl']);

	// Configure the transformer
	$proc = new XSLTProcessor;
	$proc->importStyleSheet($xsl); // attach the xsl rules

	echo $proc->transformToXML($xml);
	
	?>
	
