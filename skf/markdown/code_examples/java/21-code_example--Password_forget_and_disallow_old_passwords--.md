# Password forget and disallow old passwords
-------

## Example:


	/*
	Whenever you are developing a password forget function, these are the steps to follow
	in order to create hardened defenses.

	TABLE users
	-----------------------------------------------------------------
	| userID | userName | password |   EmailAdress   |    access    |
	-----------------------------------------------------------------   
	|   1    | Admin    | Csdar323 | info@admin.com  |     TRUE     |
	-----------------------------------------------------------------       
	|   2    | User     | Adf4fsv  | info@user.com   |     FALSE    |
	-----------------------------------------------------------------    
	|   3    | Guest    | dff4fKr  | info@guest.com  |     TRUE     |
	-----------------------------------------------------------------


	TABLE passwordForget
	-----------------------------------------------------------------------------------------   
	| forgotPasswordID |        Token            |  UserID |   Active   |     olPasswords   |
	-----------------------------------------------------------------------------------------
	|        1         |    c3ab8ff13720e....    |    1    |    YES     |      Csdar323     |
	-----------------------------------------------------------------------------------------
	|        2         |    7dd39466b3c89....    |    1    |    NO      |       ef0c4f2     |
	-----------------------------------------------------------------------------------------
	|        3         |    83d4a3960714c....    |    3    |    NO      |       dff4fKr     |
	-----------------------------------------------------------------------------------------


	As you can see we also store the old passwords into the password forget table, this
	we do in order to prevent the user from using old passwords later on in the process.

	Also use a CRON job to make sure the generated tokens for the password reset are
	expire after a certain amount of time like 20 minutes.
	*/


	package com.edw;

	import java.io.UnsupportedEncodingException;
	import java.security.InvalidKeyException;
	import java.security.NoSuchAlgorithmException;
	import java.sql.Connection;
	import java.sql.PreparedStatement;
	import java.sql.ResultSet;
	import java.sql.SQLException;

	import javax.naming.Context;
	import javax.naming.InitialContext;
	import javax.naming.NamingException;
	import javax.sql.DataSource;

	import org.apache.log4j.Logger;

	public class PasswordForget {

		final static Logger logger = Logger.getLogger(Aggregate.class);
		private String password = "" ; 
		public int userID; 
		private randomizer rand = new randomizer();
		private String active = "";
		public String token = ""; 
		
		
		public String checkValidity(String email)
		{
			boolean emptyrows = false;
			String message = ""; 
			
			//Here we connect to the database by means of a connection string as configured in the web.xml and /META-INF/context.xml 
			Connection conn = null;
			try {
			Context initContext = new InitialContext();
			Context webContext  = (Context)initContext.lookup("java:/comp/env");
			DataSource ds = (DataSource)webContext.lookup("jdbc/myJdbc");
			conn = ds.getConnection();	

			//Here we select the number of counts from aggregate column in order to verify the number of connections:
			String query = "SELECT * FROM members WHERE email = ?";
		
			//We bind the parameter in order to prevent sql injections
			PreparedStatement st = conn.prepareStatement(query);
			st.setString(1, email);
			
			// execute the query, and get a java result set
			ResultSet rs = st.executeQuery();
			
			while (rs.next())
			{
				password  = rs.getString("password");
				userID 	= rs.getInt("userID");
				email 	= rs.getString("email");
			}
			
			//If the select was not empty we will be sending an email to the user as well as
			//preparing the password forget function
			if (rs.next() == false)
			{
				emptyrows = true; 	    	  
			}
			
			rs.close();
			
			if (emptyrows == true)
			{ 	  
				message = "An email was sent to reset your password";
				/*
					Before we do anything we first set all other possible active statuses to NO
					in order to prevent an attacker creating a whole lot of tokens than FUZZING 
					the password reset token. 
					*/
				active  = "NO";   
				String query2 = "UPDATE forgetPassword SET active= ? WHERE userID= ?";
				//We bind the parameter in order to prevent SQL injections
				PreparedStatement st2 = conn.prepareStatement(query2);    
				st2.setString(1, active);
				st2.setInt(2, userID);
				
				// execute the query, and get a java result set
				st2.executeQuery();
				st2.close();
				
				String query3 = "INSERT INTO forgetPassword"
						+ " (token, userID, active, oldPasswords)"
						+ " VALUES"
						+ " (?, ?, ?, ?)";

				//We bind the parameter in order to prevent SQL injections
				PreparedStatement st3 = conn.prepareStatement(query3);  
				//Here we generate the password forget token
				String token = rand.generateToken(30);
				st3.setInt(1, userID);
				st3.setString(2, token);
				st3.setInt(3, 1);
				st3.setString(4, password);
				
				// execute the query, and get a java result set
				st3.executeQuery();
				st3.close();
				//Here we send an email to the user with the needed reset function
				String msg = "follow this link to reset your password http://example.com/index.jsp?resetLink=$token";
				SendEmail mail = new SendEmail();
				mail.sendmail(email, "Password reset", msg);   
			}
			else
			{
				/*
					We show the user the same message in order to prevent the enumeration of
					valid email addresses.
					*/
				message = "An email was sent to reset your password";  
			}
			
			rs.close();
			st.close();
			conn.close();
			
			} catch (SQLException | NamingException e) {
				logger.error("cannot search database. check query" + e.toString() );
			}
			return message; 
			//this return value can be used from SERVLETs in order to manipulate HTTP responses to send messages back to JSP pages  
		}

		public String resetPassword(String resetlink, String Password) throws InvalidKeyException, NoSuchAlgorithmException, UnsupportedEncodingException{
			hashing hasher = new hashing();
			String message = ""; 		
			/*
			Imagine the user clicked on his link with the token included and is redirected towards
			the page where he can enter his new password.
			
			Now we select the information from the forgot password function where the
			forgot tokens matches the token in the database.
			*/
			active = "YES"; 
			//Here we connect to the database by means of a connection string as configured in the web.xml and /META-INF/context.xml 
			Connection conn = null;
			try {
				
			Context initContext = new InitialContext();
			Context webContext  = (Context)initContext.lookup("java:/comp/env");
			DataSource ds = (DataSource)webContext.lookup("jdbc/myJdbc");
			conn = ds.getConnection();	

			//Here we select the number of counts from aggregate column in order to verify the number of connections:
			
			String query = "SELECT  a.userID, a.token, b.id"
					+ " FROM forgetPassword as a "
					+ "JOIN members as b"
					+ " ON a.userID = b.id WHERE token=? and Active=? ";
		
			//We bind the parameter in order to prevent SQL injections
			PreparedStatement st = conn.prepareStatement(query);
			st.setString(1, resetlink);
			st.setString(2, active);
			
			// execute the query, and get a java result set
			ResultSet rs = st.executeQuery();
			
			while (rs.next())
			{
				token     = rs.getString("token");
				userID 	= rs.getInt("userID");
			}
			
			if (resetlink.equals(token))
			{
				/*
				First we pull the password through createSalt function which enforces the input of
				secure passwords.
				*/
				String oldpassword = ""; 	
				String salt = hasher.createSalt(Password);    	
				/*
				Then we encrypt the password 
				*/	    	
				String newpassword = hasher.hashPassword(salt, Password);
				
				/*
				Finally we compare the password against other old passwords from the 
				password reset database in order to prevent the user from using old passwords 
				which could already be compromised by any means.
				*/

				//Here we select the number of counts from aggregate column in order to verify the number of connections:
				String query2 = "SELECT oldPasswords FROM forgetPassword where userID = ?";
			
				//We bind the parameter in order to prevent SQL injections
				PreparedStatement st2 = conn.prepareStatement(query2);
				st2.setInt(1, userID);
				// execute the query, and get a java result set
				ResultSet rs2 = st2.executeQuery(); 
				while (rs2.next())
				{
					oldpassword = rs2.getString("oldPasswords");
				}
				
				if (newpassword.equals(oldpassword))
				{
					message = "This was an old password please do not use this password";	
				}
				else
				{
					active = "NO";
					
					//First we update the new password for the user
					String query3 ="UPDATE members SET password=? WHERE userID=?";
					
					//We bind the parameter in order to prevent SQL injections
					PreparedStatement st3 = conn.prepareStatement(query3);	
					st3.setInt(1, userID);
					
					// execute the query, and get a java result set
					st3.executeQuery();
					
					//First we update the new password for the user
					String query4 ="UPDATE forgetPassword SET active=? WHERE userID=?";
					
					//Then we destroy the reset token by setting it's value to NO
					PreparedStatement st4 = conn.prepareStatement(query4);
					st4.setString(1, active);
					st4.setInt(2, userID); 
					
					// execute the query, and get a java result set
					st4.executeQuery();  
					
					rs2.close();
					st2.close();
					st3.close();
					st4.close();
					conn.close();
				}
				st2.close();    
			}
			st.close();
			conn.close();   
			} catch (SQLException | NamingException e) {
				logger.error("cannot search database. check query" + e.toString() );
			}
			return message; //this return value can be used from SERVLETs in order to manipulate HTTP responses to send messages back to JSP pages 
		}	
	}


