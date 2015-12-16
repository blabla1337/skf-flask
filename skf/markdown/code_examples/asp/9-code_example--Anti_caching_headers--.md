Anti-caching headers
-------

**Example:**

	    
	/*
	Add the following headers to your application head in order to prevent the browser from caching
	the following code could be used in your controller:
	*/

	Response.AppendHeader("Cache-Control", "no-cache, no-store, must-revalidate"); // HTTP 1.1.
	Response.AppendHeader("Pragma", "no-cache"); // HTTP 1.0.
	Response.AppendHeader("Expires", "0"); // Proxies.

	
	/*
	In your classes you can use the following code:
	*/

	HttpContext.Current.Response.AppendHeader("Expires", "0");
	HttpContext.Current.Response.AppendHeader("Cache-Control", "no-cache, no-store, must-revalidate");
	HttpContext.Current.Response.AppendHeader("Pragma", "no-cache");
