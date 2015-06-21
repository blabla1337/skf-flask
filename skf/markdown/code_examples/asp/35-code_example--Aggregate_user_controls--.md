Aggregate user controlls
-------

**Example:**

   	
	/*
	In order to enforce Aggregate access control protection the best method would be to 
	define your rules by means of a database structure rather than sessions or logs.
	This is due to the fact that if the user drops his session the rating would start
	al over again. 

	TABLE users
	---------------------------------------------------------------------------------   
	| userID | userName | password | privilegeID |    access    | AggregateControl	|
	---------------------------------------------------------------------------------  
	|   1    | Admin    | Csdar323 |      1      |     TRUE     |		2322		|
	---------------------------------------------------------------------------------   
	|   2    | User     | Adf4fsv  |      2      |     FALSE    |		  0			|
	---------------------------------------------------------------------------------  
	|   3    | Guest    | dff4fKr  |      3      |     TRUE     |	     125		|	
	---------------------------------------------------------------------------------

	TABLE privileges
	----------------------------------   
	| privilegeID | privilege        | 
	----------------------------------
	|     1       | edit:read:delete |
	----------------------------------
	|     2       | edit:read        |
	----------------------------------
	|     3       | read             |
	----------------------------------
	*/
		
	using System;
	using System.Collections.Generic;
	using System.Linq;
	using System.Web;
	using System.ComponentModel.DataAnnotations.Schema;
	using System.ComponentModel.DataAnnotations;
	using System.Data.SqlClient;


	namespace MvcApplication1.Models
	{
		[Table("users")]
		public class Aggregate
		{
			//Getters and setters for our user method
			[Key]
			public int userID { get; set; }
			public string userName { get; set; }
			public string password { get; set; }
			public string access { get; set; }
			public int aggregate { get; set; }
			public int privilege { get; set; }

			

			//Here we connect to the database by means of a connection string as configured in the web.config
			SqlConnection conn = new SqlConnection
			(System.Configuration.ConfigurationManager.ConnectionStrings["users"].ConnectionString);

			//The count integer is set every time the user connects to the databse to process data
			public void aggregateControll(int count)
			{
				
				//First we include the audit log class.
				AuditLog Log = new AuditLog();
			
				conn.Open();

				int controll = 0;

				//the connection has to be repported into the log files
				Log.SetLog(Session['userID'], "Connection to the database was made succesfully", "SUCCESS", "NULL" ");

				//Here we select the number of counts from aggregate column in order to verify the number of connections:
				string query = string.Format("SELECT aggregate from users WHERE userID = @userID ");
				SqlCommand cmd = new SqlCommand(query, conn);

				//We bind the parameter in order to prevent sql injections
				cmd.Parameters.AddWithValue("@userID", System.Web.HttpContext.Current.Session["userID"]);

				//Next we read the value from the database and put it into a variable
				using (SqlDataReader oReader = cmd.ExecuteReader())
				{
					while (oReader.Read())
					{
						controll = Convert.ToInt32(oReader["aggregate"]);
					}
				}

				using (SqlCommand command = conn.CreateCommand())
				{
					//We update the aggregate table in the database in order to 
					//keep track of the number of connections the user made
					count += controll;
				
					command.CommandText = "UPDATE users SET aggregate = @count WHERE userID = @userID";
					//Again we bind the parameters in order to prevent sql injections
					command.Parameters.AddWithValue("@count", count);
					command.Parameters.AddWithValue("@userID", System.Web.HttpContext.Current.Session["userID"]);

					command.ExecuteNonQuery();
				}

				/*
				Everytime the user accesses the database we keep track of the number of times he
				connected. Whenever the user passes a reasonable number he should be rejected 
				since he could be an attacker scraping your table contents and stealing company information
				You could a CRON job or stored procedure in your system in order to 
				clean the Aggregate column within certain timeframes
				*/
				HttpContext.Current.Response.Write(controll);
				if (controll > 5000)
				{
					using (SqlCommand command = conn.CreateCommand())
					{

						//this breach has to be repported into the log files
						Log.SetLog(Session['userID'], 
						"User account was locked out due to aggregate user control system", date, FAIL, HIGH");

						/*
						Whenever te reasonable number of connections the user made was surpassed we destroy all the 
						sessions to deny the user any further access to the system
						*
						HttpContext.Current.Session["authenticateUser"] = "";
						HttpContext.Current.Session.Abandon();
						HttpContext.Current.Response.Redirect("/login", true);

						/*
						Than we set his access level on his account to FALSE in order to prevent 
						him from logging in again til you did your forensics on the log files
						*/
						string access = "FALSE";
						command.CommandText = "UPDATE users SET access = @access WHERE userID = @userID";
						command.Parameters.AddWithValue("@access", access);
						command.Parameters.AddWithValue("@userID", System.Web.HttpContext.Current.Session["userID"]);

						command.ExecuteNonQuery();
					}
				}

				conn.Close();
			}

		}
	}
    
    

	
	

	

