File Upload
-------

**Example:**
	
	:::cs	
	using System;
	using System.Collections.Generic;
	using System.Linq;
	using System.Web;
	using System.Text.RegularExpressions;
	using System.IO;
	using System.Xml;

	namespace MvcApplication1.Controllers
	{ 
		public class auditLogs
		{

			private bool continueFunction = true;
			validation validate = new validation();

			//We check for form submit
			public void upload(HttpPostedFileBase file)
			{
				//We get the filename for doing different types of tests on it
				string test = file.FileName;

				/*
				First we check if the value is alphanummeric only to prevent uploading out of intended directory, 
				as wel as other injections
				*/
				if (validate.validateInput(test, "alphanummeric", "validation failed", "HIGH") == false)
				{
					continueFunction = false;
				}

				/*
				The next step would be checking if the file contains the right extension in order to prevent
				a user from uploading files which could be used to harm your system. in this example 
				we check if the last extension found in the file name is a jpg or a png. whenever
				an application just regexes for the extension an attacker could
				bypass the check by uploading an file like: "filename.jpg.php".
				*/
				string[] StrSpli = test.Split('.');
				int count = StrSpli.Count() - 1;


				if ((StrSpli[count] != "png") && (StrSpli[count] != "jpg"))
				{
					continueFunction = false;
					HttpContext.Current.Response.Write("end of function");
				}

				/*
				 If the file came through all the different checks, it is time to upload the file to your system. 
				 */
				if (continueFunction == true)
				{
					if (file != null && file.ContentLength > 0)
					{

						try
						{
							// extract only the fielname
							var fileName = Path.GetFileName(file.FileName);

							// The location of stored files should always be outside of your root
							var path = Path.Combine(@"C:\Users\Public\xml", fileName);
							file.SaveAs(path);
						}
						catch
						{
							HttpContext.Current.Response.Write("File did not upload!");
						}
					}
				}
				else
				{
					HttpContext.Current.Response.Write("end of function we returned false");
				}

				/*
				Now we check the uploaded file for the right mime-type
				We do this after the upload instead of checking the content type header sinds that header 
				can easily manipulated by an attacker. 
				 */

				string mimeType = "application/unknown";
				string ext = System.IO.Path.GetExtension(@"C:\Users\Public\xml\"+test+"").ToLower();

				Microsoft.Win32.RegistryKey regKey = Microsoft.Win32.Registry.ClassesRoot.OpenSubKey(ext);

				if (regKey != null && regKey.GetValue("Content Type") != null)
				{
					mimeType = regKey.GetValue("Content Type").ToString();
				}

				if (mimeType != "image/jpeg") 
				{   
					//If the mimetype is not valid we delete the file from the system.
					System.IO.File.Delete(@"C:\Users\Public\xml\"+test+"");
				}
			}
		}
	}
