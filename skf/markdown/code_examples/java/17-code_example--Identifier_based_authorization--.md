# Identifier-based authorization
-------

## Example:


	package com.edw;

	import java.sql.Connection;
	import java.sql.PreparedStatement;
	import java.sql.ResultSet;
	import java.sql.SQLException;
	import java.time.LocalDateTime;

	import javax.naming.Context;
	import javax.naming.InitialContext;
	import javax.naming.NamingException;
	import javax.sql.DataSource;

	import org.apache.log4j.Logger;

	public class IdentifierBased {

		public int userID  ;
		public String name;
		public String email;
		public String phone ;
		final static Logger logger = Logger.getLogger(privilegeBasedAuthentication.class);
		/*
		First we include the audit log class.
		For more detailed information see the Auditlog code example
		*/
		AuditLog Log = new AuditLog();
		
		/*
		We then do the same for aggregate user controls.
		For more detailed information see the Aggregate user control code example
		*/
		Aggregate aggregate =  new Aggregate();
		
		inputvalidation validate = new inputvalidation();
		
		/* 
		the following function return a String value that informs the appropriate 
		SERVLET to take actions such as terminate the session or take logs about 
		a certain action such as user blocking
		The following SERVLET is an example of such behavior
		
		* 	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException 
		{
			userID = request.getParameter("userID");
			
			IdentifierBased au = new IdentifierBased() ;
			String auth = au.IdentifierBasedAuthentication(pageID, userID);
			
			if (auth.equals("terminate"))
			{
				request.getSession().invalidate();
				request.setAttribute("msg","FAIL! Session terminated!");
				request.getRequestDispatcher("/login.jsp").forward(request, response);
				return;
			}
			
			else if (auth.equals("block"))
			{
				request.getSession().invalidate();
				request.setAttribute("msg","FAIL! User Blocked!");
				request.getRequestDispatcher("/login.jsp").forward(request, response);
				return;
			}
		}	
		* 
		* 
		*/
		
		public String IdentifierBasedAuthentication(int pageID, String user_id)
		{
			
			String page  = new Integer(pageID).toString();
			String identifier = "null" ; 
			/*
			First we validate if the incoming value is in fact an integer since we expect a page id number.
			If the incoming value is not a number we lockout the users since he tries to manipulate application operation.
			*/

			boolean doFunction = true;
			//see the "input validation" code example for more detailed information about this function
			if (validate.validateInput("", page, "nummeric", "Failed to get file", "HIGH") == false) { doFunction = false; }
			
			if (doFunction == false)
			{
				//First we log the fact we detected a tampering in the application operation
				Log.SetLog(user_id, "User tried to manipulate application operation", "FAIL", LocalDateTime.now(),"","HIGH");

				/*
				Set counter; if counter hits 3, the user's session must be terminated.
				After 3 session terminations the user's account must be blocked. 
				Given the high threat level, there will be immediate session termination.
				*/
				String validation = Log.counter(3);
				
				
				//the following values will be used from the SERVLET in order to handle session terminations or user blocking 
				if (validation.equals("SQL insert query error in update access" )){
						Log.SetLog(user_id, "" , "SQL insert query error in update access", LocalDateTime.now(),"",  "");
					}
					if (validation.equals("block")){
						Log.SetLog(user_id, "" , "block", LocalDateTime.now(), "",  "HIGH");
						identifier = "block";
					}
					if (validation.equals("terminate")){
						Log.SetLog(user_id, "" , "terminate", LocalDateTime.now(), "",  "HIGH");
						identifier = "terminate";
					}
			}
			
			if (doFunction == true)
			{
				//the page retrieval has to be reported into the log files
				Log.SetLog(user_id, "Connection to the database was made succesfully", "SUCCESS", LocalDateTime.now(),"","");

				//We also count the connection to the database.
				aggregate.aggregateControl(1);

				/* 
				Whenever you are checking whether a user is restricted to review certain data,
				the access restrictions should be processed from the server.
				
				The userID could be stored inside a session variable on login, and should
				be used to retrieve user data from the database when requested
				
				in order to verify if the user is allowed to look into that data:
				*/

			//Here we connect to the database by means of a connection string as configured in the web.xml and /META-INF/context.xml 
			Connection conn = null;
				try {
				
				
				Context initContext = new InitialContext();
				Context webContext  = (Context)initContext.lookup("java:/comp/env");
				DataSource ds = (DataSource)webContext.lookup("jdbc/myJdbc");
				conn = ds.getConnection();	
				
				//We also count the connection to the database.
				aggregate.aggregateControl(1);
			
				/* Here we select the users privilege level from the users table */
				String query = "SELECT * from profile WHERE userID = ? ";
			
				//execute the query, and get a java result set
				//We bind the parameter in order to prevent SQL injections
				PreparedStatement st = conn.prepareStatement(query);
				st.setInt(1, userID);
				
				//Next we read the value from the database and put it into a variable
				ResultSet rs = st.executeQuery();
				
				while (rs.next())
				{
					name  = rs.getString("name");
					email = rs.getString("email");
					phone = rs.getString("phone");
				}
				
				st.close();
				conn.close();
				
				} catch (SQLException | NamingException e) {
					logger.error("cannot search database. check query" + e.toString() );
				}
			
				this.setEmail(email);
				this.setName(name);
				this.setPhone(phone);
			}
			return identifier;
			
		}


		public String getName() {
			return name;
		}


		public void setName(String name) {
			this.name = name;
		}


		public String getEmail() {
			return email;
		}


		public void setEmail(String email) {
			this.email = email;
		}


		public String getPhone() {
			return phone;
		}


		public void setPhone(String phone) {
			this.phone = phone;
		}

	}

