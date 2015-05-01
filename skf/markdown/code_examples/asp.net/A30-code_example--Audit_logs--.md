
Audit logs
-------

**Example:**

    /*
    The log function does not have to be complicated as long as you log at least these 6 values
    */

	using System;
	using System.Collections.Generic;
	using System.Linq;
	using System.Web;
	using System.IO;
	using System.Data.SqlClient;
	using System.ComponentModel.DataAnnotations.Schema;
	using System.ComponentModel.DataAnnotations;

	namespace MvcApplication1.Controllers
	{
		[Table("counter")]
		public class auditLogs
		{

			//Getters and setters for our user method
			[Key]
			public int countID { get; set; }
			public int userID  { get; set; }
			public int count   { get; set; }
			public int blocker { get; set; }

			//Here we connect to the database by means of a connection string as configured in the web.config
			SqlConnection conn = new SqlConnection(System.Configuration.ConfigurationManager.ConnectionStrings["users"].ConnectionString);

			public void SetLog(string session, string message, string ipadress, string state, string threat)
			{

				using (StreamWriter writer = new StreamWriter(@"C:\Users\Public\xml\logs.txt", true))
				{
					writer.WriteLine(session + " - " + message + " - " + ipadress + " - " + state + " - " + threat);
				}
			}

			public void counter(int counting)
			{

				/*
				First we select the counts from the count table in order to verify if the user session should be terminated
				or that the user should be locked out.
				*/
				conn.Open();

				string query = string.Format("SELECT * from counter WHERE userID = @userID ");
				SqlCommand cmd = new SqlCommand(query, conn);

				//We bind the parameter in order to prevent sql injections
				cmd.Parameters.AddWithValue("@userID", System.Web.HttpContext.Current.Session["userID"]);

				//Next we read the value from the database and put it into a variable
				using (SqlDataReader oReader = cmd.ExecuteReader())
				{
					while (oReader.Read())
					{
						count   = Convert.ToInt32(oReader["count"]);
						blocker = Convert.ToInt32(oReader["blocker"]);
					}
				}

				//We add the counting to the database results for the final value
				int finalCount = counting += count;
				int finalBlock = counting += blocker;

				/*
				then we update the count table in order to keep track of the number of counts
				*/
				try
				{
					using (SqlCommand command = conn.CreateCommand())
					{

						command.CommandText = "UPDATE counter set count = @count, blocker = @blocker WHERE userID = @userID";

						//Again we bind the parameters in order to prevent SQL injections
						command.Parameters.AddWithValue("@count", finalCount);
						command.Parameters.AddWithValue("@blocker", finalCount);
						command.Parameters.AddWithValue("@userID", System.Web.HttpContext.Current.Session["userID"]);

						command.ExecuteNonQuery();
					}
				}
				catch (SqlException e)
				{
					if (e.Source != null)
					{
						System.Web.HttpContext.Current.Response.Write("SQL insert query error in update counter");

					}
				}
				conn.Close();


				/*
				After these steps we check whether the user should be blocked, whenever the count is equal to 12 we take
				further actions by means of blocking the users account and terminating his session
				*/

				if (finalBlock >= 12)
				{
					try
					{
						using (SqlCommand command = conn.CreateCommand())
						{
							conn.Open();
							string access = "FALSE";
							command.CommandText = "UPDATE users set access = @access WHERE userID = @userID";

							//Again we bind the parameters in order to prevent SQL injections
							command.Parameters.AddWithValue("@access", access);
							command.Parameters.AddWithValue("@userID", System.Web.HttpContext.Current.Session["userID"]);

							command.ExecuteNonQuery();

							HttpContext.Current.Session["authenticateUser"] = "";
							HttpContext.Current.Session.Abandon();
						}
					}
					catch (SqlException e)
					{
						if (e.Source != null)
						{
							System.Web.HttpContext.Current.Response.Write("SQL insert query error");
							System.Web.HttpContext.Current.Response.Write(e);
						}
					}
				}
				/*
				If the count hit three, the user get's a warning by means of a session termination.
				Whenever this termination occurs three times he will lock out his account.
				*/
				if (finalCount >= 3)
				{
					HttpContext.Current.Session["authenticateUser"] = "";
					HttpContext.Current.Session.Abandon();
					HttpContext.Current.Response.Redirect("/login", true);
				}
			}
		}
	}
