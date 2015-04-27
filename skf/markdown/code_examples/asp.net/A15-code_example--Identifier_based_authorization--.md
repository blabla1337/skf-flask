
Identifier-based authorization
-------

**Example:**


	using System;
	using System.Collections.Generic;
	using System.Linq;
	using System.Web;
	using System.ComponentModel.DataAnnotations.Schema;
	using System.ComponentModel.DataAnnotations;
	using System.Data.SqlClient;


	namespace MvcApplication1.Models
	{
		[Table("profile")]
		public class users
		{
			//Getters and setters for our user method
			[Key]
			public int userID { get; set; }
			public string name { get; set; }
			public string email { get; set; }
			public string phone { get; set; }

			/*
			First we include the audit log class.
			For more detailed information see the Auditlog code example
			*/
			AuditLog Log = new AuditLog();

			/*
			We then do the same for aggregate user controlls.
			For more detailed information see the Aggregate user controll code example
			*/
			Aggregate aggregate =  new Aggregate();

			//Here we connect to the database by means of a connection string as configured in the web.config
			SqlConnection conn = new SqlConnection(System.Configuration.ConfigurationManager.ConnectionStrings["users"].ConnectionString);

			//The count integer is set every time the user connects to the databse to process data
			public void IdentifierBasedAuthentication(int pageID)
			{
				conn.Open();

				bool doFunction = true;

				/*
				First we validate if the incomming value is in fact an integer since we expect a page id number.
				If the incomming value is not a number we lockout the users since he tries to manipulate application operation.
				*/
				if (validate.validateInputNumeric(pageID) == false) { doFunction = false; }

				if (doFunction == false)
				{
					//First we log the fact we detected a tampering in the application operation
					Log.SetLog(Session['userID'], "User tried to manipulate application operation", date, FAIL, HIGH");

					/*
					Set counter; if counter hits 3, the user's session must be terminated.
					After 3 session terminations the user's acount must be blocked. 
					Given the high threat level, there will be immediate session termination.
					*/
					Log.Counter(3);
				}

				if (doFunction == true)
				{
					//the page retrieval has to be repported into the log files
					Log.SetLog(Session['userID'], "Connection to the database was made succesfully", date, SUCCESS, NULL");

					//We also count the connection to the database.
					aggregate.aggregateControll(1);

					/* 
					Whenever you are checking whether a user is restricted to review certain data,
					the acces restrictions should be proccessed serverside.
					The userID could be stored inside a session variable on login, and should be used to retrieve userdata from the database when requested
					in order to verify if the user is allowed to look into that data:
					*/
					string query = string.Format("SELECT * from profile WHERE userID = @userID ");
					SqlCommand cmd = new SqlCommand(query, conn);

					//We bind the parameter in order to prevent sql injections
					cmd.Parameters.AddWithValue("@userID", System.Web.HttpContext.Current.Session["userID"]);

					//Next we read the value from the database and put it into a variable
					using (SqlDataReader oReader = cmd.ExecuteReader())
					{
						while (oReader.Read())
						{
							name  = oReader["name"].ToString();
							email = oReader["email"].ToString();
							phone = oReader["phone"].ToString();
						}
					}
				}
			}
		}
	}
	
	
