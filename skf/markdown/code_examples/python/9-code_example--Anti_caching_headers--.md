
Anti-caching headers
-------

**Example:**



	    <?php
	    
		/*
		Add the following headers to your application head in order to prevent the browser from caching
		*/

		header("Cache-Control: no-store, no-cache, must-revalidate"); // HTTP/1.1
		header("Cache-Control: post-check=0, pre-check=0", false);
		header("Pragma: no-cache"); // HTTP/1.0 

		?>


	