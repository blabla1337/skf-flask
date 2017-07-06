X-Content-Type-Options Header
-------

**Example:**

In order to set the "X-Content-Type-Options" header you'll have to add the 
following code to the head of your application, the following code could be used in your controller:

	:::cs
	Response.AppendHeader("X-Content-Type-Options", "nosniff"); 
    	
In your classes you can use the following code:
	
	:::cs
	HttpContext.Current.Response.AppendHeader("X-Content-Type-Options", "nosniff"); 
