Path traversal
-------

**Example:**

	using System;
	using System.Collections.Generic;
	using System.Linq;
	using System.Web;
	using System.Text.RegularExpressions;
	using System.IO;

	namespace MvcApplication1.Controllers
	{
		public class rewrite
		{
			auditLogs Log = new auditLogs();
			inputvalidation validate = new inputvalidation();
			whitelist listme = new whitelist();

			public void getFiles(string getFile)
			{
				/*
				First, we want to filter the filenames for expected values. For this example we use only use 0-9
				Whenever the values are tampered with, we can assume an attacker is trying to inject malicious input.           
				*/
				bool validated = true;

				//see the "input validation" code example for more detailed information about this function
				if (validate.validateInput(getFile, "nummeric", "Failed to get file", "HIGH") == false) { validated = false; }

				/*
				see the "whitelisting" code example for more detailed information about this function
				Let's assume there are three files named 1,2,3
				*/
				
				if (listme.whitelisting("1,2,3", getFile) == false) { validated = false; }

				//Only if the pattern was true we allow the variable into the streamreader function
				if (validated == true)
				{
					try
					{
						StreamReader sr = new StreamReader(@"C:\Users\Public\xml\" + getFile + ".txt", true);
						String FileText = sr.ReadToEnd().ToString();

						sr.Close();
					}
					catch(DirectoryNotFoundException e)
					{
						if (e.Source != null)
						{
							HttpContext.Current.Response.Write("catching file failed");
						}
					}
				}
				else
				{
					HttpContext.Current.Response.Write("invalid userinput was detected!");
				}
			}
		}
	}
	

