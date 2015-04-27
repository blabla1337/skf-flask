	BELANGRIJK, VOEG HIER NOG FFKES EEN REGEX VOOR DE SPECIALE TEKENS AAN TOE!
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

				string error = "";
				string password = Request["password"];

				bool complete = true;

				/*
				Here we define the minimal expexted value's for your password.
				The password must at least contain a Capital letter, a normal letter, a special character
				a number and must be at least 8 characters long
				*/
				string[] pattern = new string[3] { "[0-9]", "[A-Z]", "[a-z]" };

				if (Request.Form["submit"] != null)
				{
					foreach (string validation in pattern)
					{
						//Now if the regex detects any missing character than we will set complete to false
						Regex regex = new Regex(validation);
						Match match = regex.Match(password);

						if (!match.Success)
						{
							error = "You did not enter a valid password";
							complete = false;
						}
					}

					try
					{   
						/*
						Also very important is the fact that you have to take into consideration that
						Password1! is a valid password according to password standards. This however is not the case since
						this password is included in almost every dictionairy attack system. So we have to prevent the user from using these
						weak passwords, this we do by defining these bad passwords in a text file and compare the user's password with the
						bad passwords defined in the text file.
						*/
						
						StreamReader sr = new StreamReader(Path.Combine(Server.MapPath("~"), @"C:\Users\Public\xml\bad.txt"));
						String FileText = sr.ReadToEnd().ToString();

						string[] strTemp = FileText.Split(',');

						foreach (string value in strTemp)
						{
							if (value == password)
							{
								error = "Your password was a bad password!";
								complete = false;
							}
						}

						sr.Close();
					}
					catch
					{
						Response.Write("catching file failed");
					}

				
					//The last stap is checking the password length to see if it is 8 characters or bigger
					if (password.Length < 8)
					{
						error = "The password was to short";
						complete = false;

					}

					if (complete == true)
					{
						//Do further operation
						Response.Write("Good job password was ok!");
					}
					else
					{
						Response.Write(error);
					}
				}

				return View();
			}

		}
	} 

