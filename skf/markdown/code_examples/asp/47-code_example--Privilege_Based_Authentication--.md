 Privilege based authentication
-------

## Example:
   	
   	/*
    For privilege based authentication we need an extra tabel in your database in order to write the users privileges to.

    TABLE users
    ---------------------------------------------------------------------------------    
    | userID | userName | password | privilegeID |    access	| AggregrateControl	|
    ---------------------------------------------------------------------------------   
    |   1	 | Admin	| Csdar323 |	  1		 | 	   TRUE		|		2336		|
    ---------------------------------------------------------------------------------   	
    |	2	 | User		| Adf4fsv  |	  2		 |	   FALSE	|		 0			|
    ---------------------------------------------------------------------------------   
    |	3	 | Guest	| dff4fKr  |	  3		 |	   TRUE		|		135			|
    ---------------------------------------------------------------------------------   

    TABLE privileges
    ----------------------------------   
    | privilegeID | privilege 		 | 
    ----------------------------------
    |     1	 	  | edit:read:delete |
    ----------------------------------
    |	  2	 	  | edit:read		 |
    ----------------------------------
    |	  3	 	  | read			 |
    ----------------------------------

    Now instead of using roles in sessions we rather want to assign privileges to users 
    by means of a Database-Based Authentication system. 
    Now we can easily assign a user certain privileges for him to access.
    */
    
	using System;
	using System.Collections.Generic;
	using System.Linq;
	using System.Web;
	using System.Data.SqlClient;
	using System.ComponentModel.DataAnnotations;
	using System.Web.SessionState;
	using System.Text.RegularExpressions;

	namespace MvcApplication1.Controllers
	{
		public class privilegeBasedAuthentication
		{
			//Getters and setters for our user method
			[Key]
			public int userID { get; set; }
			public string username { get; set; }
			public string password { get; set; }
			public string access { get; set; }
			public string salt { get; set; }
			public int privilege { get; set; }

			//First we include the audit log class.
			auditLogs Log = new auditLogs();

			//Here we connect to the database by means of a connection string as configured in the web.config
			SqlConnection conn = 
			new SqlConnection(System.Configuration.ConfigurationManager.ConnectionStrings["users"].ConnectionString);

			public string privileges()
			{
				string privileges = "";

				conn.Open();

				//the connection has to be repported into the log files
				Log.SetLog("Null", "Connection to the database was made succesfully", "SUCCESS", "NULL");

				/*
				Here we select the users privelege level from the users tabele
				NOTE: query has to be in one line but could not fit screen otherwise
				*/
				string query = string.Format("
				SELECT a.username, a.password, a.privilegeID, b.privelegeID, 
				b.privelege FROM users as a JOIN priveleges as b ON a.privilegeID = b.privelegeID 
				WHERE a.userID =@userID and a.access='TRUE'");
				
				SqlCommand cmd = new SqlCommand(query, conn);

				//We bind the parameter in order to prevent sql injections
				cmd.Parameters.AddWithValue("@userID", System.Web.HttpContext.Current.Session["userID"]);

				//Next we read the value from the database and put it into a variable
				using (SqlDataReader oReader = cmd.ExecuteReader())
				{
					while (oReader.Read())
					{
						privileges = Convert.ToString(oReader["privilege"]);
					}
				}

				return privileges;
			}

			//Here we check the priveleges string against the permissions needed to perform the actions
			public bool validator(string priveleges, string ispermitted)
			{

				bool privileged = false;
				string[] privDB = priveleges.Split(':');
				string[] permission = ispermitted.Split(':');

				int count = permission.Length;
				int countsucces = 0;

				foreach (string priv in privDB)
				{
					//We count the number of times the regex hits your privelege
					Regex regex = new Regex(priv);
					if (priv != "")
					{
						Match match = regex.Match(ispermitted);
						if (match.Success)
						{
							countsucces += 1;
						}
					}
				}

				//Whenever the count is bigger or equal to the results we know the user was permitted
				if (countsucces >= count)
				{
					privileged = true;
					//the connection has to be repported into the log files
					Log.SetLog(Convert.ToString(System.Web.HttpContext.Current.Session["userID"]), 
					"User did have the right priveleges!", "SUCCESS", "NULL");
				}
				else
				{
					//the connection has to be repported into the log files
					Log.SetLog("Null", "User did not have the right priveleges!", "FAIL", "NULL");

					//Terminiate session since the user tries to tamper his privileges
					Log.setCounter(3);
					privileged = false;
				}
				return privileged;
			}
		}
	}

	/*
    if ever there are new 'roles' added to the system you can easily asign them the needed privileges without 
    having to add new roles throughought your entire system. This system takes a little more planning up ahead but 
    it enforces higher level of security.
    */
    
    
