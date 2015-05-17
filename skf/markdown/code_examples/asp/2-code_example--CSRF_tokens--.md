
CSRF tokens
-------

**Example:**

	
    /*
    For CSRF tokens we used a sepperate class outside of the normal controller, since
    it must be re-used on severall locations throughout the application
    
	First after a succsesfull validation of a user login, the application must also start a session
	which contains the "cross site request forgery" token.
    */
    
	/*
	For generating the token we want to use a secure cryptographic function
	in order to use RNGCryptoServiceProvider we must first add :
	using System.Security.Cryptography;
	*/
	RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider();

	//Then we generate a long value token containing a high entropy
	byte[] buffer = new byte[128];

	rng.GetBytes(buffer);

	//Then we base64 encode the string
	string csrftoken = System.Convert.ToBase64String(buffer);

	System.Web.HttpContext.Current.Session["CSRF"] = csrftoken; 


	/*
	The next step is implementing this random token in each form field as a hidden input parameter
	and send it to a function which checks if the submitted token is equal to the one set after succesfull validation.
	*/
	

	<form method="post" action="/Home/csrf">
    <input type="text" name="testValue" />
    <input type="hidden" name="csrftoken" value="@Session["CSRF"];" />
    <input type="submit" value="submit the form" />
    </form>
	
	//here we are sending the token towards the function which does the token validation    
	public void checkCSRF(string token)
	{
	
		string Sessiontoken = Convert.ToString(System.Web.HttpContext.Current.Session["CSRF"]);
	
		//We compare the incomming token with the current session Token which was assigned on login
		if(Sessiontoken != token)
		{	
			/*
			If there was no match the authentication session will be emptied and sessions
			Will be abandoned, we redirect the user towards the login page.
			*/
		
			HttpContext.Current.Session["authenticateUser"] = "";
			HttpContext.Current.Session.Abandon();
			HttpContext.Current.Response.Redirect("/login", true);            
		}           
	
	}     
	


	