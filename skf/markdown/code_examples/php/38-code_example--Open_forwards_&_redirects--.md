# Open forwards & redirects
-------

## Example:


   	<?php

    	/*
    	When using forwards & redirects you should make sure the URL is being explicitly
    	declared in the code and cannot be manipulated by an attacker like:
    	*/

    	header("location:redirectpage.php");

    	/*
    	Generally you should avoid getting input into the redirect which could contain
    	user-input by any means. if for any reason this may not be feasible than you
    	should make a whitelist input validation for the redirect like so:
    	send("value1,value2,etc", $_GET['redirectParam'], "3")
    	*/

    	class redirecting{
    		public function send($whiteListing, $inputParam, $countLevel){

    			//Include the classes of which you want to use objects from
    			include_once("classes.php");

    			$whitelist = new whitelisting();

    			/*
    			We want to whitelist the paged for expected values, in this example they are,
    			page1,page2 etc.. for more information about whitelisting see "white-listing" in the code examples:
    			*/
    			if($whitelist->checkpattern($whiteListing, $inputParameter, $countLevel) == true){
    				header("location:".$inputParam."");
    			}			
    		}
      }

    ?>
