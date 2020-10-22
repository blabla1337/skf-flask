SQL query
-------

## Example:


	/*
	In c# MVC there are a lot of different methods in order to process your SQL query's to 
	the database. Most of them are already secure by design and leave little to no room for
	error such as SQL to LinQ or doing your database handling by the entity framework.

	However if you want to use the sql command method you must use this functionality by
	means of prepared statements in order to prevent sql injections.
	*/


	using System;
	using System.Collections.Generic;
	using System.Linq;
	using System.Web;
	using System.ComponentModel.DataAnnotations.Schema;
	using System.ComponentModel.DataAnnotations;
	using System.Data.SqlClient;
	using System.Web.SessionState;


	namespace MvcApplication1.Models
	{
		[Table("users")]
		public class users
		{
			//Getters and setters for our user method
			[Key]
		
			public int userID      { get; set; }
			public string username { get; set; }
			public string email    { get; set; }

			//First we include the audit log class.
			//AuditLog Log = new AuditLog();

			//Here we connect to the database by means of a connection string as configured in the web.config
			SqlConnection conn = new 
			SqlConnection(System.Configuration.ConfigurationManager.ConnectionStrings["users"].ConnectionString);

			public void selectStatement()
			{   
				//Open the database connection
				conn.Open();

				try
				{   
					string query = string.Format("SELECT * from users WHERE userId = @userID ");
					SqlCommand cmd = new SqlCommand(query, conn);

					//We bind the parameter in order to prevent sql injections
					cmd.Parameters.AddWithValue("@userID", System.Web.HttpContext.Current.Session["userID"]);

					//Next we read the value from the database and put it into a variable
					using (SqlDataReader oReader = cmd.ExecuteReader())
					{
						while (oReader.Read())
						{
							username = oReader["username"].ToString();
							email    = oReader["email"].ToString();

						}
					}
					//close the connection again
					conn.Close();
				}
				catch(SqlException e){
					if (e.Source != null)
					{
						System.Web.HttpContext.Current.Response.Write("Invalid select query");
						throw;
					}
				}
			}

			public void insertStatement()
			{   
				//We open the connection towards the database
				conn.Open();

				try
				{
					using (SqlCommand command = conn.CreateCommand())
					{ 
					
						command.CommandText = "INSERT INTO users(username,email) VALUES(@param1,@param2)";  
					
						//Again we bind the parameters in order to prevent SQL injections
						command.Parameters.AddWithValue("@param1", username);  
						command.Parameters.AddWithValue("@param2", email);   

						command.ExecuteNonQuery(); 
					}
				}
				catch(SqlException e){
					if(e.Source != null)
					{
						System.Web.HttpContext.Current.Response.Write("SQL insert query error");
						throw;
					}
				}

				//we close the connection again
				conn.Close();
			}
		}
	}
	
	



	
