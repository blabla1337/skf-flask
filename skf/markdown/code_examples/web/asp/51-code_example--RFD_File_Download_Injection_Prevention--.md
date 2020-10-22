RFD and file download injections
-------

## Example:
	

	using System;
	using System.Collections.Generic;
	using System.Linq;
	using System.Web;
	using System.Net;
	using System.Data.SqlClient;

	namespace MvcApplication1.Controllers
	{
		public class downloadFiles
		{
			//Here we connect to the database by means of a connection string as configured in the web.config
			SqlConnection conn = new
			SqlConnection(System.Configuration.ConfigurationManager.ConnectionStrings["download"].ConnectionString);

			private string fileName;
			private bool proceed = true;
			private string mimeType;

			validation validate = new validation();
			whitelist whitelist = new whitelist();

			public void downloadUserFiles(int fileID)
			{
				/*
				For the sake of example we only allow the users to download their own files
				by identifier based sql query's. As you can see we select the filename
				by its id. in this case we prevent direct userinput into the disposition header.
				*/

				//Since we only expect an integer back from the user we validate the userinput for integers
				if (validate.validateInput(Convert.ToString(fileID), "numeric", "invalid input", "HIGH") == false) { proceed = false; }

				if (proceed == true)
				{
					conn.Open();
					string query = string.Format("SELECT * FROM downloads WHERE userID=@userID and fileID=@fileID");
					SqlCommand cmd = new SqlCommand(query, conn);

					//We bind the parameter in order to prevent sql injections
					cmd.Parameters.AddWithValue("@userID", Session["userID"]);
					cmd.Parameters.AddWithValue("@fileID", fileID);

					//Next we read the value from the database and put it into a variable
					using (SqlDataReader oReader = cmd.ExecuteReader())
					{
						while (oReader.Read())
						{
							fileName = Convert.ToString(oReader["fileName"]);
							mimeType = Convert.ToString(oReader["mimeType"]);
						}
					}
					if (fileName != null)
					{
						try
						{
							/*
							We also define the mimetype per download file.
							This is because whenever a user can only download images it is not necessary to set
							an uncommon content-type header for it.
							NOTE: These mimetypes should not be stored based upon the mimetype which was send 
							the response header when the user uploaded the file. This value can be easily 
							manipulated with an intercepting proxy. You should get the mimetype from the file
							itself after it was stored on the server.
							*/
							System.Web.HttpResponse response = System.Web.HttpContext.Current.Response;
							response.ClearContent();
							response.Clear();
							response.ContentType = mimeType;
							response.AppendHeader("Cache-Control", "no-cache");
							response.AddHeader("Content-Disposition", "attachment; filename=" + fileName + ";");
							response.WriteFile(@"\\servername\folder1\folder2\folder3\" + fileName + "");
							response.Flush();
							response.End();
						}
						catch (NullReferenceException e){
							if (e.Source != null)
							{
								HttpContext.Current.Response.Write("error!");
							}
						}
					}
				}
			}

			public void fixedDownloads(string download)
			{
				/*
				The second example is for whenever you are providing users with fixed downloads
				such as manuals etc. We do not only check if the file just exists, because that would
				allow an attacker to also download important other files from your server, so instead
				we whitelist them.
				*/
				if (whitelist.whitelisting("file1.txt,file2.txt", download) != false)
				{
					System.Web.HttpResponse response = System.Web.HttpContext.Current.Response;
					response.ClearContent();
					response.Clear();
					response.ContentType = "text/plain";
					response.AppendHeader("Cache-Control", "no-cache");
					response.AddHeader("Content-Disposition", "attachment; filename=" + download + ";");
					response.WriteFile(@"\\servername\folder1\folder2\folder3\" + download + "");
					response.Flush();
					response.End();
				}
			}
		}
	}
