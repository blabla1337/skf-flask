X-Path Query
-------

**Example:**

	:::cs
	using System;
	using System.Collections.Generic;
	using System.Linq;
	using System.Web;
	using System.Diagnostics;
	using System.Xml;
	using System.Xml.XPath;
	namespace MvcApplication1.Controllers
	{
		public  class Class1
		{

			public string selectPath(string employeeID)
			{
				 /*
				 In order to prevent x-path injections we have to treat these query's similar as 
				 to the sql query's. An option would be to use a precompiled XPath query.
				 But since this is a third party library i consider it untrusted and would
				 rather use our own crafted escaping function.
			 
				 NOTE: if you want to look into the precompiled x-path library you can find more
				 detailed information about it on: http://www.tkachenko.com/blog/archives/000385.html
				 */

				 /*
				 As with every injection prevention we first focus on the expected user values
				 in this case we expect an integer we use our single input validation method for integers
				 See the "input validation" code example for more detailed information.
				 */

				bool continueFunction = true;
				string foo = "";

				inputvalidation validate = new inputvalidation();

				//Here we put the variable in our inputvalidation method in order to prevent untrusted userinput from parsing
				//NOTE: logging and countering is also done in your validation method
				if (validate.validateInput(Convert.ToString(employeeID), "nummeric", "x-path input validation", "HIGH") == false) 
				{ continueFunction = false; }

				//Only if our validation function returned true we put the userinput in the function
				if (continueFunction == true)
				{
					XmlDocument xmldoc = new XmlDocument();
					try
					{
						xmldoc.Load(@"C:\Users\Public\xml\register.xml");
						foo = xmldoc.SelectSingleNode("/Employees/Employee[ID=" + employeeID + "]").InnerText;
					}
					catch (Exception e)
					{
						if (e.Source != null)
						{
							System.Web.HttpContext.Current.Response.Write("Oops something went wrong");
							throw;
						}
					}
				}
				else
				{
					System.Web.HttpContext.Current.Response.Write("unexpected userinput detected!");
				}
					return foo;
			}
		}
	}

The same principle as seen in the example applys for whenever you expect alphanumeric values or even names. 
The only difference is that you take another validation type from the input validation function 
i.e whenever you must accept names like o'reily you must encode the quotes.See the "input validation" code example
for more detailed information about these escape methods.
