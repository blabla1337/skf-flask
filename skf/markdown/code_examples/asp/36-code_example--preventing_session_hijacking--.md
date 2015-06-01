Session hijacking
-------

**Example:**


	/*
	As soon as a user logs into your application you must store his session id as wel as his
	IP adress allong with his userID. This information will be used later on in your application in order to
	identify possible session hijacking.

	TABLE track_sessions
	---------------------------------------------------------------------------------
	| TrackID | userID |		   	   SESSION 		            |     Ip adress	    | 
	---------------------------------------------------------------------------------
	|   1     | 1      | 	79dcd529c0f5e01a9bfb2425c52036c6    |	123.45.67.89	|   
	---------------------------------------------------------------------------------
	|   2     | 1      | 	79dcd529c0f5e01a9bfb2425c52036c6    |	123.45.67.81	|
	---------------------------------------------------------------------------------
	|   3     | 2      | 	c80959d3ea4c166413774e45375ac2a1    |	987.65.43.21	|
	---------------------------------------------------------------------------------

	In order to prevent session hijacking there are a couple of defense strategies
	which combined are a hardened defense.  
	*/

	/*
	First we implement the strict transport security header, this is in order to prevent
	users from accessing your application over an unprotected connection.
	*/

	//Example of the strict transport security header:
	Response.AppendHeader("Strict-Transport-Security", "max-age=31536000");


	//If all present and future subdomains will be HTTPS:
	Response.AppendHeader("Strict-Transport-Security" max-age=31536000, "includeSubDomains");

	/*
	Recommended: If the site owner would like their domain to be included in the HSTS preload 
	list maintained by Chrome (and used by Firefox and Safari), then use:
	*/

	Response.AppendHeader("Strict-Transport-Security", "max-age=31536000", "includeSubDomains" ,"preload");

	/*
	The `preload` flag indicates the site owner's consent to have their domain preloaded. 
	The site owner still needs to then go and submit the domain to the list. the preload list
	enforces the browser to always present your application on HTTPS even on the first time
	the user hits your application
	*/

	/*
	Then we set the httpOnly flag
	(see "HttpOnly" in the code examples for more details about implementation)
	*/
	
	/*
	Then we set the flag for session timeout
	(see "Timeout" in the code examples for more details about implementation)
	*/
	
	/*
	Then we set the session secure flag 
	(see "Secure flag" in the code examples for more details about implementation)
	*/
	
	/*
	On login we also add another cookie with a random value to the application in order to
	prevent an attacker to fixate an ASPSESSION id on your users and hijack their sessions
	(This code example can be found in the "Login functionality" for more detailed information)
	*/
	
	
	/*
	NOTE: On applications that require high level security, there should never be an
	remember me functionality implemented.
	*/


	/*
	Now imagine the scenario after the login of the user (see the "login functionality" in
	the code examples for more details). Whenever the user is logged in, the users ip adress 
	and session id are also stored in the database these values are used in order to verify 
	if there are mulitple users active on the same session. 
	If so, we can let the user decide to terminate the session and terminate the
	other assigned sessions.
	*/
	
	using System;
	using System.Collections.Generic;
	using System.Linq;
	using System.Web;
	using System.ComponentModel.DataAnnotations.Schema;
	using System.ComponentModel.DataAnnotations;
	using System.Data.SqlClient;
	using System.Web.SessionState;


	namespace MvcApplication1.Models
	{
		[Table("users")]
		public class users
		{
			//Getters and setters for our user method
			[Key]
			public int trackingID  { get; set; }
			public int userID      { get; set; }
			public string token    { get; set; }
			public string ipadress { get; set; }

			//First we include the audit log class.
			AuditLog Log = new AuditLog();

			//Here we connect to the database by means of a connection string as configured in the web.config
			SqlConnection conn = new 
			SqlConnection(System.Configuration.ConfigurationManager.ConnectionStrings["users"].ConnectionString);

			//The count integer is set every time the user connects to the databse to process data
			public void checkSession()
			{
				if ((System.Web.HttpContext.Current.Session["authenticateUser"] != "isLoggedin") || 
				(System.Web.HttpContext.Current.Session["authenticateUser"] == ""))
				{
					HttpContext.Current.Response.Redirect("/login", true);
				}

				conn.Open();

				string query = string.Format("SELECT * from tracking WHERE userId = @userID ");
				SqlCommand cmd = new SqlCommand(query, conn);

				//We bind the parameter in order to prevent sql injections
				cmd.Parameters.AddWithValue("@userID", System.Web.HttpContext.Current.Session["userID"]);
			
				//Next we read the value from the database and put it into a variable
				using (SqlDataReader oReader = cmd.ExecuteReader())
				{
					while (oReader.Read())
					{
						session  = oReader["sessiom"].ToString();
						ipadress = oReader["ipadress"].ToString();

						if ((System.Web.HttpContext.Current.Session["ASPsessionID"].ToString() != session) && 
						(ipadress != HttpContext.Current.Request.ServerVariables["REMOTE_ADDR"]))
						{   
							//We log the muliple users on the system 
							Log.SetLog(Session['userID'], "Mulitple users with same session id detected", date, FAIL, MOD");

							/*
							We redirect the user to a page which alerts him as well as gives him the option to destroy the 
							mulitple sessions if he does not trust them
							*/
							HttpContext.Current.Response.Redirect("/Home/multipleUsers", true);
						}
					}
				}
			}
		}
	}    

	/*
	the only thing left to do now is to update your track_sessions table by inserting
	the ipadress, sessionID and userID if you want to accept the other sessions as valid.
	Otherwise the user just has to terminate his current session in order to lock out the
	other sessions.
	*/

	?>

