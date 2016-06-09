Content Type Headers
-------

**Example:**

In order to set the Content-type header, you'll have to add the following 
code to the head of your application, the following code could be used in your controller:
    
	:::cs
	Response.AppendHeader("Content-Type:text/html", "charset=UTF-8"); 

In your classes you can use the following code:

	:::cs	
	HttpContext.Current.Response.AppendHeader("Content-Type:text/html", "charset=UTF-8");
	
