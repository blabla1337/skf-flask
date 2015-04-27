	
Path traversal
-------

**Example:**

	using System;
	using System.Collections.Generic;
	using System.Linq;
	using System.Web;
	using System.Web.Mvc;
	using System.Security.Cryptography;
	using System.IO;
	using System.Text.RegularExpressions;


	namespace MvcApplication1.Controllers
	{
		public class HomeController : Controller
		{
			public ActionResult getFile()
			{
				string getFile = Request.QueryString["getFile"];

				/*
				First, we want to filter the filenames for expected values. For this example we use only a-z/0-9
				Whenever the values are tampered with, we can assume an attacker is trying to inject malicious input.           
				*/

				Regex regex = new Regex(@"\W|_");

				Match match = regex.Match(getFile);
				if (match.Success)
				{
					//this breach has to be repported into the log files
					Log.SetLog(Session['userID'], "Untrusted userinput was detected in the file get contents function in HOME/CSRF, date, FAIL, HIGH");

					 /*
					 Set counter; if counter hits 3, the user's session must be terminated.
					 After 3 session terminations the user's acount must be blocked.
					 For detailed information see the "Audit logs" in code examples.
					 In this example the user was tampering the application's operation so immediate lockout will be followed
					 */

					Setcounter.count(3);
				}

				/*
				Here we define a whitelist of files we want the user allow to access to, in this case all 
				path traversal patterns are terminated with since it does not comply with the pre-defined withelist
				*/ 
				string[] allowed = new string[] { "test", "file2", "file3" };
			
				//To catch the user submitting evil requests we count the number of times the foreach hits false
				int count = 1;
				int counter = allowed.Length;

				foreach (string item in allowed)
				{
					//For validation if the file returned true
					bool validated = false;
				
					//If filename is equal to the pre-defined items
					if (getFile == item)
					{
						validated = true;
					}
			 
					//Only if the pattern was true we allow the variable into the streamreader function
					if (validated == true)
					{
						try
						{
							StreamReader sr = new StreamReader(Path.Combine(Server.MapPath("~"), @"" + getFile + ".txt"));
							String FileText = sr.ReadToEnd().ToString();
						
							//Here we count -1 in order to prevent from triggering the log functions
							count = -1;
							Response.Write(FileText);

							sr.Close();
						}
						catch
						{   
							Response.Write("catching file failed");
						}
					}

					//Here we add up the counts, if they are equal we know the function did not hit a valid filename
					count++;
				
					if (counter == count)
					{
						//this breach has to be repported into the log files
						Log.SetLog(Session['userID'], "Untrusted userinput was detected in the file get contents function in HOME/CSRF, date, FAIL, HIGH");

						/*
						Set counter; if counter hits 3, the user's session must be terminated.
						After 3 session terminations the user's acount must be blocked.
						For detailed information see the "Audit logs" in code examples.
						In this example the user was tampering the application's operation so immediate lockout will be followed
						*/

						Setcounter.count(3);
					}

				}               

					return View();
			}

		}
	}
