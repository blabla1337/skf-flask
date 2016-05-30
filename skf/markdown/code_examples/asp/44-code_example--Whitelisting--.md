 Whitelisting
-------

**Example:**

	:::cs
	using System;
	using System.Collections.Generic;
	using System.Linq;
	using System.Web;

	namespace MvcApplication1.Controllers
	{
		public class whitelist
		{
			//Include auditlog class
			auditLogs Log = new auditLogs();

			public bool whitelisting(string allowed, string input)
			{
				/*
				Here we define a whitelist of pages we want the user allow to be redirected to, all
				patterns are terminated whenever they not comply with the pre-defined withelist
				*/

				string[] pattern = allowed.Split(',');

				//For validation if the file returned true
				bool validated = false;

				//To catch the user submitting evil requests we count the number of times the foreach hits false
				int count = 0;
				int countArray = 0;

				int counter = allowed.Length;

				foreach (string item in pattern)
				{
					//If filename is equal to the pre-defined items
					if (input == item)
					{
						validated = true;
						count = -1;
					}

					//Here we add up the counts, if they are equal we know the function did not hit a valid filename
					count++;
					countArray++;
				}

				if (countArray == count)
				{
					//this breach has to be reported into the log files
					Log.setLog(HttpContext.Current.Session["userID"], "Audit log message!", "FAIL", "HIGH");

					Log.setCounter.count(3);
				}
				return validated;
			}
		}
	}
