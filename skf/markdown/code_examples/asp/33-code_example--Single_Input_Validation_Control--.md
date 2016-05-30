Single Input Validation Control
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
		public class inputvalidation
		{

			public bool validateInput(string input, string type, string logMessage, string theatLevel)
			{
				/*
				Than we want to filter the filenames for expected values. For this example we use only a-z/0-9
				Whenever the values are tampered with, we can assume an attacker is trying to inject malicious input.           
				*/

				string validator = "";
		   
				switch (type)
				{
					case "alphanumeric":
						validator = "^[a-zA-Z0-9]+$";                  
						break;
					case "nummeric":
						validator = "^[0-9]*$";
						break;
				}
			
				Regex regex = new Regex(validator);
				bool validate = false;


				Match match = regex.Match(input);
				if (match.Success)
				{
					//If there was a match this function returns false
					validate = true;

					//this breach has to be repported into the log files
					Log.SetLog(Session['userID'], logMessage, date, "FAIL", theatLevel);

					/*
					Set counter; if counter hits 3, the user's session must be terminated.
					After 3 session terminations the user's acount must be blocked.
					For detailed information see the "Audit logs" in code examples.
					*/

					Log.count(1);

				}
				else
				{
					Log.SetLog(Session['userID'], logMessage, date(), "SUCCESS", "NULL");
				}
				return validate;
			}
		}

	}

	//Usage:
	if(validate.validateInput(Convert.ToString(employeeID), "nummeric", "input validation", "HIGH") == false) 
	{ 
		continueFunction = false; 
	}
	
