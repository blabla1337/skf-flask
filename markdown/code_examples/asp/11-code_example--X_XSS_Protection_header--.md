X-XSS-Protection header
-------

**Example:**


    /*
    In order to set the X-XSS-Protection header, you'll have to add the following 
    code to the head of your application, the following code could be used in your controller:
    */
    
    Response.AppendHeader("X-XSS-Protection:1", "mode=block"); 

	/*
	In your classes you can use the following code:
	*/
	
	HttpContext.Current.Response.AppendHeader("X-XSS-Protection:1", "mode=block");
	

