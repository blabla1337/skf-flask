X-Content-Type-Options header
-------

## Example:


    <?php

    /*
    In order to set the "X-Content-Type-Options" header you'll have to add the 
    following code to the head of your application, the following code could be used in your controller:
    */
    
    Response.AppendHeader("X-Content-Type-Options", "nosniff"); 
    
	/*
	In your classes you can use the following code:
	*/
	
	HttpContext.Current.Response.AppendHeader("X-Content-Type-Options", "nosniff"); 
	

    ?>

