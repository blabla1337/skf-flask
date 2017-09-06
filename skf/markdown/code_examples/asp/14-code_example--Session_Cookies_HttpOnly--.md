Session cookies HttpOnly
-------

## Example:

	/*
	Whenever a session is started, the "httpOnly" option should always be set
	in order to prevent session data to be stolen by attackers.
	
    By default, .NET 2.0 sets the HttpOnly attribute for:
    Session ID,
    Forms Authentication cookie

    In .NET 2.0, HttpOnly can also be set via the HttpCookie object for all custom application 
    cookies via web.config in the system.web/httpCookies element
	*/
	
	<httpCookies httpOnlyCookies="true"> 

    //Or programmatically
	//C# Code:

	HttpCookie myCookie = new HttpCookie("AuthToken", guid);
	HttpContext.Current.Response.Cookies.Add(myCookie);
	myCookie.HttpOnly = true;

	

	
