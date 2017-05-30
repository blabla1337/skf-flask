Aggregate User Control 
-----------------------

***Example:***

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/*
In order to enforce Aggregate access control protection the best method would be to 
define your rules by means of a database structure rather than sessions or logs.

Verify the system can protect against aggregate or continuous access of secured functions, 
resources, or data. For example, consider the use of a resource governor to limit the number 
of edits per hour or to prevent the entire database from being scraped by an individual user.

TABLE users
---------------------------------------------------------------------------------   
| userID | userName | password | privilegeID |    access    |     aggregate	    |
---------------------------------------------------------------------------------  
|   1    | Admin    | Csdar323 |      1      |     TRUE     |       2322        |
---------------------------------------------------------------------------------   
|   2    | User     | Adf4fsv  |      2      |     FALSE    |         0         |
---------------------------------------------------------------------------------  
|   3    | Guest    | dff4fKr  |      3      |     TRUE     |        125        |   
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

The following code snippets can be used in relation with this class in order to have a full implemented example 

HTML/JSP page index.jsp


<%@page contentType="text/html" pageEncoding="UTF-8"%>

<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Insert Value</title>
    </head>
    <body>
        <form method="post" action="aggregateControl">
        <table>
            <tr>
                <td>Name  : </td>
                <td><input type="text" id="name" name="name" /></td>
            </tr>  
            <tr>
            	<td>Surname : </td>
            	<td><input type="text" id="surname" name="surname" /></td>
            </tr>
            <tr>
            	<td>Password : </td>
            	<td><input type="text" id="password" name="password" /></td>
            </tr>               
            <tr>
            	<td><input type="hidden" id="userID" value="2" name="userID" /></td>
            </tr>         
        	<tr>
                <td colspan="2"><input type="submit" /></td>               
           	</tr>
        	</table>
         </form>     
    </body>
</html>



Servlet 


the following code snippet can be used in relation with the following servlet snippet


public class AggregateControl extends HttpServlet{
	private static final long serialVersionUID = 1L;
    public aggregateControl() {
        super();
    }
	
	final static Logger logger = Logger.getLogger(AggregateControl.class);
	private String userName;
	private String password;
	private String userID;

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException 
	{
		
		userName = request.getParameter("name");
		userID = request.getParameter("userID");
		Aggregate ag = new Aggregate();
		ag.setUserName(userName);
		ag.setUserID(userID);
	    boolean invalidate_sessions = ag.aggregateControl(0);
		
		if (invalidate_sessions == true)
		{
			request.getSession().invalidate();			
		}
		
		doGet(request, response);
		
		}
		
output logs indicating that user has been logged out after many database connections  

[ .... ] 

2016-11-24 11:17:55 INFO  Aggregate:277 - Connection to the database was made successfully   User: ddd  User ID:  2
2016-11-24 11:18:07 INFO  Aggregate:277 - Connection to the database was made successfully   User: ddd  User ID:  2
2016-11-24 11:18:15 INFO  Aggregate:277 - Connection to the database was made successfully   User: ddd  User ID:  2
2016-11-24 11:18:23 INFO  Aggregate:277 - Connection to the database was made successfully   User: ddd  User ID:  2
2016-11-24 11:18:32 INFO  Aggregate:277 - Connection to the database was made successfully   User: ddd  User ID:  2
2016-11-24 11:18:39 INFO  Aggregate:277 - Connection to the database was made successfully   User: ddd  User ID:  2
2016-11-24 11:18:49 INFO  Aggregate:240 -  User account was locked out due to aggregate user control system  User: ddd  Userid ID:  2
2016-11-24 11:18:49 INFO  Aggregate:277 - Connection to the database was made successfully   User: ddd  User ID:  2
 
 
*/

package com.edw;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.sql.DataSource;

import org.apache.log4j.Logger;

public class NewAggregate {
	
	public String userName;
	public String password;
	public String userID;
	private int control = 0;
	
	
	final static Logger logger = Logger.getLogger(NewAggregate.class);

	public boolean aggregateControl(int count)
	{
		
			boolean invalidate_sessions = false; 
				
			 //Here we connect to the database by means of a connection string as configured in the web.xml and /META-INF/context.xml 
			Connection conn = null;
		    try {
					
			Context initContext = new InitialContext();
			Context webContext  = (Context)initContext.lookup("java:/comp/env");
			DataSource ds = (DataSource)webContext.lookup("jdbc/myJdbc");
			conn = ds.getConnection();	

			  //Here we select the number of counts from aggregate column in order to verify the number of connections:
		      String query = "SELECT aggregate from users WHERE userID = ?";
		   
		      PreparedStatement st = conn.prepareStatement(query);
		      st.setString(1, userID);
		      
		      // execute the query, and get a java result set
		      //We bind the parameter in order to prevent SQL injections

		      ResultSet rs = st.executeQuery();
		      
		      while (rs.next())
		      {
		        control  = rs.getInt("aggregate");
		
		      }

		      //We update the aggregate table in the database in order to 
	          //keep track of the number of connections the user made
	          count = control + 1;
	          
		      // create the java mysql update prepared statement
		      String query2 = "UPDATE users SET aggregate = ? WHERE userID = ?";
		      PreparedStatement preparedStmt2 = conn.prepareStatement(query2);
		      preparedStmt2.setInt(1, count);
		      preparedStmt2.setString(2, userID);

		      // execute the java prepared statement
		      preparedStmt2.executeUpdate();
		      
					/*
		            Every time the user accesses the database we keep track of the number of times he
		            connected. Whenever the user passes a reasonable number he should be rejected 
		            since he could be an attacker scraping your table contents and stealing company information
		            You could a CRON job or stored procedure in your system in order to 
		            clean the Aggregate column within certain time frames
		            */
	          
	          if ( control > 5000)
	          {
	            
	                  //this breach has to be reported into the log files
	        	      logger.info( " User account was locked out due to aggregate user control system" + "  User: " + userName + "  Userd ID:  " +  userID);

	                  /*
	                  Whenever the reasonable number of connections the user made was surpassed we destroy all the 
	                  sessions to deny the user any further access to the system. This session invalidation is controlled from the SERVLET 
	                  
	                  */
	        	      invalidate_sessions = true; 
	                 
	                  /*
	                  Than we set his access level on his account to FALSE in order to prevent 
	                  him from logging in again till you did your forensics on the log files
	                  */
	        	      
	                  // create the java MySql update prepared statement
	    
	                  int access = 0; //0 is considered as FALSE in MySQL
	        	      String query3 = "UPDATE users SET access = ? WHERE userID = ?";
	        	      PreparedStatement preparedStmt3 = conn.prepareStatement(query3);
	        	      preparedStmt3.setInt(1, access);
	        	      preparedStmt3.setString(2, userID);

	        	      // execute the java prepared statement
	        	      preparedStmt3.executeUpdate();
	        	      preparedStmt3.close();
	        	      
	          }
	          st.close();
	          preparedStmt2.close();
	          conn.close();

			} catch (SQLException | NamingException e) {
				 logger.error("cannot update database. check query" + e.toString() );

			}	      
	       		
		    //the connection has to be reported into the log files
			if(logger.isInfoEnabled()){
				logger.info("Connection to the database was made succesfully " + "  User: " + userName + "  Userd ID:  " +  userID);
			}
			else{
			logger.error("Couldnt connect to database - " +  "  User: " + userName + "  Userd ID:  " +  userID);
			}
			
		return invalidate_sessions;
	}

	public String getUserName() {
		return userName;
	}

	public void setUserName(String userName) {
		this.userName = userName;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public String getUserID() {
		return userID;
	}

	public void setUserID(String userID) {
		this.userID = userID;
	}

}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`