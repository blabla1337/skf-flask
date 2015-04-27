
XML injection prevention
-------

**Example:**

   		
	using System;
	using System.Collections.Generic;
	using System.Linq;
	using System.Web;
	using System.Web.Mvc;
	using System.Xml;
	using System.IO;
	using System.Text.RegularExpressions;

	namespace MvcApplication1.Controllers
	{
		public class HomeController : Controller
		{
			public ActionResult Index()
			{   
				/*
				 First we import our inputvalidation controll class. for more detailed information about 
				 input validation check the code examples for "Input validation" & "Single input validation".
				 */ 
				inputValidationControll validate = new inputValidationControll();

				if (Request.Form["submit"] != null)
				{
					//Here we validate the userinput.
					string name = Request["name"];
					string lastName = Request["lastName"];
					string gender = Request["gender"];

					bool doFunction = true;

					//If the function returns false, we do not execute the function
					if (validate.validateInput(name)     == false) { doFunction = false; }
					if (validate.validateInput(lastName) == false) { doFunction = false; }
					if (validate.validateInput(gender)   == false) { doFunction = false; }

					if (doFunction == true)
					{
						//Only after validation we proceed to the XMLwriter class where we insert the parameters
						using (XmlWriter writer = XmlWriter.Create(@"C:\Users\Public\xml\register.xml"))
						{
							writer.WriteStartElement("person");
							writer.WriteElementString("name", name);
							writer.WriteElementString("lastname", lastName);
							writer.WriteElementString("gender", gender);
							writer.WriteEndElement();
							writer.Flush();
						}
					}
				}

				/*
				Now we prevented malicious userinput from comming into your XML file.
				NOTE: Do not forget to also properly encode your input as a last line of defense, 
					  also In this example the XmlReader diable's external entities by default.
					  If you should choose another parser make sure your parser disables these entities 
					  in order to prevent XXE injections.
				*/
				using (XmlReader reader = XmlReader.Create(@"C:\Users\Public\xml\register.xml"))
				{
					while (reader.Read())
					{
						// Only detect start elements.
						if (reader.IsStartElement())
						{
							// Get element name and switch on it.
							switch (reader.Name)
							{
								case "name":
									string attribute = reader["name"];
									if (reader.Read())
									{
										ViewBag.name = HttpUtility.HtmlEncode(reader.Value.Trim());
									}
									break;

								case "lastname":
									string lastName_ = reader["lastname"];
									if (reader.Read())
									{
										ViewBag.lastname = HttpUtility.HtmlEncode(reader.Value.Trim());
									}
									break;

								case "gender":
									string gener_ = reader["gender"];
									if (reader.Read())
									{
										ViewBag.gender = HttpUtility.HtmlEncode(reader.Value.Trim());
									}
									break;
							   
									/*
									When using Razor view engine (which is the default view engine in ASP.NET), 
									using the '@' character to display values in your view it will automatically encode the displayed value. 
									This means that you don't have to use encoding.
									*/
							}
						}
					}
				}
			 
				return View();
			}

		}
	}
