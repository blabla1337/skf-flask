# User registration SQL truncation prevention
-------

## Example:


	/*
	In order to prevent Column truncation SQL injection Solution we have to make sure the
	applications structural logic does not mismatches with the database structural logic.
	To achieve this imagine the follow example of a database structure of a users table

	TABLE users
	------------------------------------------------------------
	|        *Name*        |    *Type*        |    *Extra*     |
	------------------------------------------------------------
	|        userID        |    Int(11)       | AUTO_INCREMENT |
	------------------------------------------------------------
	|       Username       |    char(21)      |                |
	------------------------------------------------------------
	|       Password       |  Varchar(255)    |                |
	------------------------------------------------------------
	|      PrivilegeID     |    Int(11)       |                |
	------------------------------------------------------------
	*/


	package com.edw;

	import java.io.UnsupportedEncodingException;
	import java.security.InvalidKeyException;
	import java.security.NoSuchAlgorithmException;
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

	public class RegisterUser {
		
		private AuditLog Log = new AuditLog();
		private hashing hash = new hashing();
		final static Logger logger = Logger.getLogger(RegisterUser.class);
		
		public boolean userCheck(String username){
			
			boolean isTrue = false; 
			//Here we connect to the database by means of a connection configured in the web.xml and /META-INF/context.xml 
			Connection conn = null;
			try {
			
			
			Context initContext = new InitialContext();
			Context webContext  = (Context)initContext.lookup("java:/comp/env");
			DataSource ds = (DataSource)webContext.lookup("jdbc/myJdbc");
			conn = ds.getConnection();	
			

			//Here we select the number of counts from aggregate column in order to verify the number of connections:
			String query = "SELECT * FROM members WHERE username = ?";
		
			//We bind the parameter in order to prevent SQL injections
			PreparedStatement st = conn.prepareStatement(query);
			st.setString(1, username);
			
			// execute the query, and get a java result set


			ResultSet rs = st.executeQuery();
			
			if (!rs.isBeforeFirst() && !rs.next())
			{
				isTrue = true;
			}
			
			st.close();
			conn.close();
			
			} catch (SQLException | NamingException e) {
				logger.error("cannot search database. check query" + e.toString() );
			}
			return isTrue;
		}
		
		public boolean userRegister(String username, String password, int privID){

			boolean isTrue = false;
			
			/*
				Whenever the user gains the ability to register himself or change his user
				credentials you must always enforce the application to compare the length of the
				submitted string against the length of the allowed string length in your database
				structure in order to prevent SQL column truncation.
				*/
			
			int length = username.length(); 
				/*
				We now compare the length of the username against the allowed string length in
				The database structure
				*/
			if(length >= 21){
					//If length is to large the function must return false and the result must be logged.
					Log.SetLog(username, "Username was to long!", "FAIL!", LocalDateTime.now(), null);
	
				}
			
			//If true then register the user!       
			if(this.userCheck(username) == true){
				isTrue = true;
				
				//Then we encrypt the password
				String salt = "";
				String passhash = "";
				try {
					salt = hash.createSalt(password);	    	 
					passhash = hash.hashPassword(salt, password);
				
				} catch (InvalidKeyException | NoSuchAlgorithmException | UnsupportedEncodingException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}   
				
				//Here we connect to the database by means of a connection string as configured in the web.xml and /META-INF/context.xml 
				Connection conn = null;
					try {	
					Context initContext = new InitialContext();
					Context webContext  = (Context)initContext.lookup("java:/comp/env");
					DataSource ds = (DataSource)webContext.lookup("jdbc/myJdbc");
					conn = ds.getConnection();	
					
					//After successful validation we enter the new user into the database
					String query = "INSERT INTO users"
							+ " (Username, Password, PrivilegeID)"
							+ " VALUES"
							+ " (?, ?, ?)";
						
					PreparedStatement st = conn.prepareStatement(query);
					
					st.setString(1, username);
					st.setString(2, passhash);
					st.setInt(3, privID);

					ResultSet rs = st.executeQuery();
							
					rs.close();
					st.close();
					conn.close();
					
					} catch (SQLException | NamingException e) {
						logger.error("cannot search database. check query" + e.toString() );
					}

				}
			else
			{
				Log.SetLog("", "Username" + username + " already exists!", "FAIL!", LocalDateTime.now(), null);
				isTrue = false ;
			}

			return isTrue;
		}
		
	}


