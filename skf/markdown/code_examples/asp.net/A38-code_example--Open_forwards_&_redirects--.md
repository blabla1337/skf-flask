
Open forwards & redirects
-------

**Example:**
	
	/*
	When using forwards & redirects you should make sure the URL is being explicitly 
	declared in the code and cannot be manipulated by an attacker like:
	*/
	
	HttpContext.Current.Response.Redirect("/login", true);
	
	/*
	Generally you should avoid getting input into the redirect which could contain
	user-input by any means. if for any reason this may not be feasible than you 
	should make a whitelist input validation for the redirect like so:
	*/
	
	     
	using System;
	using System.Collections.Generic;
	using System.Linq;
	using System.Web;


	namespace MvcApplication1.Controllers
	{

		public class OpenForwards
		{
			public void openForwards(string redirect)
			{
				/*
			   Here we define a whitelist of pages we want the user allow to be redirected to,  all 
			   patterns are terminated whenever they not comply with the pre-defined withelist
			   */

				string[] allowed = new string[] { "userInfo", "messages", "etc" };

				//To catch the user submitting evil requests we count the number of times the foreach hits false
				int count = 1;
				int counter = allowed.Length;

				foreach (string item in allowed)
				{
					//For validation if the file returned true
					bool validated = false;

					//If filename is equal to the pre-defined items
					if (redirect == item)
					{
						validated = true;
					}

					//Only if the pattern was true we allow the variable into the streamreader function
					if (validated == true)
					{
						try
						{
							HttpContext.Current.Response.Redirect(redirect, true);
						}
						catch
						{
							HttpContext.Current.Response.Write("redirect failed");
							count = -1;
						}
					}

					//Here we add up the counts, if they are equal we know the function did not hit a valid filename
					count++;

					if (counter == count)
					{
						//this breach has to be repported into the log files
						Log.SetLog(HttpContext.Current.Session["userID"], "Untrusted userinput was detected in the file get contents function in HOME/CSRF", "FAIL", "HIGH");

						/*
						Set counter; if counter hits 3, the user's session must be terminated.
						After 3 session terminations the user's acount must be blocked.
						For detailed information see the "Audit logs" in code examples.
						In this example the user was tampering the application's operation so immediate lockout will be followed
						*/

						Setcounter.count(3);
					}
				}
			}
		}
	}

