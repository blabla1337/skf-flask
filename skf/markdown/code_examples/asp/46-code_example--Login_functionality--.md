Login functionality
-------

## Example:
	

	using System;
	using System.Collections.Generic;
	using System.Linq;
	using System.Web;
	using System.Data.SqlClient;
	using System.ComponentModel.DataAnnotations;
	using System.Web.SessionState;

	namespace MvcApplication1.Controllers
	{
		public class login
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

			//Second we include the password hash.
			hashing hash = new hashing();

			//Third we include the random password/token class.
			randomizer CSRF = new randomizer();

			//Last we include the random inputvalidation class.
			inputvalidation validate = new inputvalidation();

			public bool loginUser()
			{
				//Here we connect to the database by means of a connection string as configured in the web.config
				SqlConnection conn = new SqlConnection(System.Configuration.ConfigurationManager.ConnectionStrings["users"].ConnectionString);

				bool loggedin = false;
            	string passwordHash = "";
            	string userId = "";
				conn.Open();

				//we also validate the username input, if it was bad we empty the string:
				if (validate.validateInput(username, "alphanumeric", "Error in username", "LOW", 0) != true) { username = ""; }

				//Here we select the user from the users table
				string query = string.Format("SELECT * from users WHERE username = @name ");
				SqlCommand cmd = new SqlCommand(query, conn);

				//We bind the parameter in order to prevent sql injections
				cmd.Parameters.AddWithValue("@name", username);

				//Next we read the value from the database and put it into a variable
				using (SqlDataReader oReader = cmd.ExecuteReader())
				{
					while (oReader.Read())
					{
						username = Convert.ToString(oReader["username"]);
						passwordHash = Convert.ToString(oReader["password"]);
						salt = Convert.ToString(oReader["salt"]);
						userId = Convert.ToString(oReader["userID"]);
					}
				}

				/*
				We validate the password see "Password storage(salting stretching hashing)" in the code examples
				for more detailed information:
				*/
				if (hash.Validate(passwordHash, salt, password) == true)
				{
					/*
					This is is to prevent session fixation, after login we create a new cookie which
					we than use to authenticate. This value can not be fixated since it is set after 
					login.
				 
					create a a new GUID and save into the session:
					*/

					string guid = Guid.NewGuid().ToString();
					HttpContext.Current.Session["AuthToken"] = guid;

					// now create a new cookie with this guid value
					HttpContext.Current.Response.Cookies.Add(new HttpCookie("AuthToken", guid));

					//the connection has to be reported into the log files
					Log.SetLog("Null", "login was OK!", "SUCCESS", "NULL");

					/*
					Now we create a random value for our CSRF tokens. See "Random password/token generation" in
					the code examples for more detailed information:
					*/
					string CSRftoken = CSRF.generate(25);
					System.Web.HttpContext.Current.Session["CSRF"] = CSRftoken;

					//Set an accessor session.
					System.Web.HttpContext.Current.Session["Authenticated"] = "access";

					/*
					Put id in a session for query identifier based authentication
					See "identifier based authentication" code example for more information
					 */
					System.Web.HttpContext.Current.Session["userID"] = userId;

					loggedin = true;
				}else{
					//the connection has to be repported into the log files
					Log.SetLog("null", "Login failed!", "FAIL", "NULL");
					loggedin = false;
					HttpContext.Current.Response.Redirect("/login", true);
				}
				return loggedin;
			}

			//In this method we do a check if the sessions are ok
			public void checkSession()
			{
				//We use this try catch for whenever the cookie is dropped
				try
				{   
					//Check sessions and cookies to see if they match
					if (!HttpContext.Current.Session["AuthToken"].ToString().Equals(
						HttpContext.Current.Request.Cookies["AuthToken"].Value)
						|| (HttpContext.Current.Session["Authenticated"] != "access"))
					{
						HttpContext.Current.Response.Redirect("/login", true);
					}
				}
				catch (NullReferenceException e){
					if (e.Source != null)
					{   
						HttpContext.Current.Response.Redirect("/login", true);
						HttpContext.Current.Session["Authenticated"] = "";
						HttpContext.Current.Session.Clear();
						HttpContext.Current.Session.Abandon();
						HttpContext.Current.Session.RemoveAll();
					}
				}
			}
		}
	}

