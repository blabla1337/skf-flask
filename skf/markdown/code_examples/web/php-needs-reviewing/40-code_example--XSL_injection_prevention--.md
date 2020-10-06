# XSL injection prevention
-------

## Example:


    <?php

	/*
	In order to prevent XSL injections you must enforce strict policy's whenever the
	files are loaded from a source controlled by an possible attacker.

	Let's say for example that the user can choose from several XSL files on your application.

	ABC.xsl arranges your employee names on alphabetical order
	CBA.xsl does not care and just shows the input by order of your XML file.

	Before we want to attach the XSL files to the style sheet we first want to
	do validation on the request to make sure the included file was one of our own pre
	defined files, example:
	including("file1.xsl,file2.xsl,etc", $_GET['xslfile'], "3")
	*/

	class includeXSL{
		public function including($whiteListing, $inputParam, $countLevel){

			//Include the classes of which you want to use objects from
			include_once("classes.php");

			$whitelist = new whitelisting();

			$continue = true;

			/*
			We want to whitelist the paged for expected values, in this example they are,
			page1,page2 etc.. for more information about whitelisting see "white-listing" in the code examples:
			*/
			if($whitelist->checkpattern($whiteListing, $inputParam, $countLevel) == false)
			{$continue = false;}

			//If all went good we do the function
			if($continue == true){
				# LOAD XML FILE
				// Load the XML source
				$xml = new DOMDocument;
				$xml->load('test.xml');

				$xsl = new DOMDocument('1.0','UTF-8');
				$xsl->load($inputParam);

				// Configure the transformer
				$proc = new XSLTProcessor;
				$proc->importStyleSheet($xsl); // attach the xsl rules

				echo $proc->transformToXML($xml);
			}
		}
	}

    ?>
