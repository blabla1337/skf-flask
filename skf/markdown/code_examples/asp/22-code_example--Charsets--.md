Charsets
-------

**Example:**

In order to set the "Charsets" header you'll have to add the 
following code to the head of your application, the following code could be used in your controller 
for by example, text/html:
	
	:::cs
	Response.AppendHeader("Content-Type: text/html", "charset=utf-8"); 
    
In your classes you can use the following code:

	:::cs	
	HttpContext.Current.Response.AppendHeader("Content-Type: text/html", "charset=utf-8"); 
	
Or directly into your html markup:
	
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	


	
