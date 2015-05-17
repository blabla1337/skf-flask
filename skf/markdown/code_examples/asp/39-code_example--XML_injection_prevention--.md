
XML injection prevention 
-------

**Example:**

   		
	using System;
	using System.Collections.Generic;
	using System.Linq;
	using System.Web;
	using System.Text.RegularExpressions;
	using System.IO;
	using System.Xml;

	namespace MvcApplication1.Controllers
	{
		public class storeXML
		{
			public void storeFuncion(string name, string lastName, string gender)
			{
				/*
				First we import our inputvalidation controll class. for more detailed information about 
				input validation check the code examples for "Input validation" & "Single input validation".
				*/
				inputValidationControll validate = new inputValidationControll();

				bool doFunction = true;

				//If the function returns false, we do not execute the function
				
				//see the "input validation" code example for more detailed information about this function
				if (validate.validateInput(name, "alphanummeric", "Invalid userinput name", "HIGH") == false)     { doFunction = false; }
				if (validate.validateInput(lastName, "alphanummeric", "Invalid userinput name", "HIGH") == false) { doFunction = false; }
				if (validate.validateInput(gender, "alphanummeric", "Invalid userinput name", "HIGH") == false)    { doFunction = false; }

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

		}
	}
	/*
	Now we prevented malicious userinput from comming into your XML file.
	NOTE: Do not forget to also properly encode your input as a last line of defense, 
		  also In this example the XmlReader diasble's external entities by default.
		  If you should choose another parser make sure your parser disables these entities 
		  in order to prevent XXE injections.
	  */
          

    


