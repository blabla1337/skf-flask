Logout
-------

**Example:**

	:::cs
	using System;
	using System.Collections.Generic;
	using System.Linq;
	using System.Web;

	namespace MvcApplication1.Controllers
	{
		public class logout
		{
			public void logOut()
			{   
				//We clear abandon and remove all sessions before we start
				HttpContext.Current.Session.Clear();
				HttpContext.Current.Session.Abandon();
				HttpContext.Current.Session.RemoveAll();

				//Double check this and empty your session manually
				HttpContext.Current.Session["Authenticated"] = "";

				//Clear the aspsessionID
				if (HttpContext.Current.Request.Cookies["ASP.NET_SessionId"] != null)
				{
					HttpContext.Current.Response.Cookies["ASP.NET_SessionId"].Value = string.Empty;
					HttpContext.Current.Response.Cookies["ASP.NET_SessionId"].Expires = DateTime.Now.AddMonths(-20);
				}

				//Clear our custom set cookie.
				if (HttpContext.Current.Request.Cookies["AuthToken"] != null)
				{
					HttpContext.Current.Response.Cookies["AuthToken"].Value = string.Empty;
					HttpContext.Current.Response.Cookies["AuthToken"].Expires = DateTime.Now.AddMonths(-20);
				}

				HttpContext.Current.Response.Redirect("/login", true);
			}
		}
	}
