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
				whitelist listMe = new whitelist();

				bool validated = true;
			
				//For more information about white-listing see the "Whitelisting" code example:
				if (listMe.whitelisting("page1,page2,page3", redirect) == false) { validated = false; }
			
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
					}
				}
			}
		}
	}
	

