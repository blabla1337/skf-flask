Encoding
-------

**Example:**

	:::cs	
	using System;
	using System.Collections.Generic;
	using System.Linq;
	using System.Web;
	using System.Text.RegularExpressions;

	namespace MvcApplication1.Controllers
	{
		public class encoding
		{
			public string encoder(string input, string allowed)
			{
				/*
				We can specify also special characters which where allowed in order to keep
				track of any unwanted special characters, even though they will be encoded
				violations of your system must have consequences!
				*/
				Regex regex = new Regex("^[a-zA-Z0-9" + allowed + "]+$");
				Match match = regex.Match(input);
				if (!match.Success)
				{
					Log.SetLog(Session['userID'], logMessage, date, "FAIL", theatLevel);
					Log.count(1);
					input = "Error";
				}
				//We return the userinput encoded
				return HttpUtility.HtmlEncode(input);
			}
		}
	}
