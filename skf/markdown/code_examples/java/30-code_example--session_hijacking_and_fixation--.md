# Session hijacking and fixation 
-------

## Example:


package com.edw;
/*
As soon as a user logs into your application you must store his session id as wel as his
IP adress allong with his userID. This information will be used later on in your application in order to
identify possible session hijacking.

TABLE track_sessions
---------------------------------------------------------------------------------
| TrackID | userID |               session                  |     ipaddress     | 
---------------------------------------------------------------------------------
|   1     | 1      |    79dcd529c0f5e01a9bfb2425c52036c6    |   123.45.67.89    |   
---------------------------------------------------------------------------------
|   2     | 1      |    79dcd529c0f5e01a9bfb2425c52036c6    |   123.45.67.81    |
---------------------------------------------------------------------------------
|   3     | 2      |    c80959d3ea4c166413774e45375ac2a1    |   987.65.43.21    |
---------------------------------------------------------------------------------

In order to prevent session hijacking there are a couple of defense strategies
which combined are a hardened defense.  
*/

/*
First we implement the strict transport security header, this is in order to prevent
users from accessing your application over an unprotected connection.
*/

//Example of the strict transport security header:
// response.setHeader("Strict-Transport-Security", "max-age=31536000");


//If all present and future subdomains will be HTTPS:
//response.setHeader("Strict-Transport-Security", "max-age=31536000; includeSubdomains;");


/*
Recommended: If the site owner would like their domain to be included in the HSTS preload 
list maintained by Chrome (and used by Firefox and Safari), then use:
*/

// response.setHeader("Strict-Transport-Security", "max-age=31536000; includeSubdomains; preload");


/*
The `preload` flag indicates the site owner's consent to have their domain preloaded. The preload list
enforces the browser to always present your application on HTTPS even on the first time
the user hits your application
*/

/*
Then we set the httpOnly flag
(see "HttpOnly" in the code examples for more details about implementation)
*/

/*
Then we set the flag for session timeout
(see "Timeout" in the code examples for more details about implementation)
*/

/*
Then we set the session secure flag 
(see "Secure flag" in the code examples for more details about implementation)
*/

/*
On login we also add another cookie with a random value to the application in order to
prevent an attacker to fixate an JSSESSION id on your users and hijack their sessions
(This code example can be found in the "Login functionality" for more detailed information)
*/

/*
NOTE: On applications that require high level security, there should never be a
remember me functionality implemented.
*/

/*
Now imagine the scenario after the login of the user (see the "login functionality" in
the code examples for more details). Whenever the user is logged in, the users ip address 
and session id are also stored in the database these values are used in order to verify 
if there are mulitple users active on the same session. 
If so, we can let the user decide to terminate the session and terminate the
other assigned sessions.
*/

import java.io.IOException;
import java.sql.*;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import javax.sql.DataSource;

import org.apache.log4j.Logger;

public final class SessionHijack extends HttpServlet{
	
	private static final long serialVersionUID = 1L;
    
    public SessionHijack() {
        super();
    }
	
	//First we include the audit log class.
	final static Logger logger = Logger.getLogger(SessionHijack.class);
		
	private int userID;
	private String ipaddress;
	private String sess ;
	private String user_ID ;
	private String trackID ;

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException 
	{
		
		user_ID = request.getSession().getId(); 
		
		//Here we connect to the database
		
		Connection conn = null;
		
		if ((request.getSession().getAttribute("authenticateUser") != "isLoggedin") || 
	            (request.getSession().getAttribute("authenticateUser") == ""))
	            {			
			 		RequestDispatcher rd =
			        request.getRequestDispatcher("/login");
			        rd.forward(request, response);
	             	               
	            }
		
		try {
			Context initContext = new InitialContext();
			Context webContext  = (Context)initContext.lookup("java:/comp/env");
			DataSource ds = (DataSource)webContext.lookup("jdbc/myJdbc");
			conn = ds.getConnection();	
			
			String query = "SELECT * from tracking WHERE userId = ?";
			
		    PreparedStatement st = conn.prepareStatement(query);
		    st.setString(1, user_ID);
		      
		    // execute the query, and get a java resultset
		    //We bind the parameter in order to prevent sql injections

		      ResultSet rs = st.executeQuery();
		      
		      //Next we read the value from the database and put it into a variable
		      while (rs.next())
		      {
		        sess  = rs.getString("session");
		        ipaddress = rs.getString("ipaddress");
		        trackID =  rs.getString("TrackID");
		        
		         
		        if ((request.getSession().getAttribute("JSSESSIONID").toString() != sess) && 
	                    (ipaddress != request.getRemoteAddr()))
	                    {   
						
						    //We log the muliple users on the system 
	                      	logger.info("Mulitple users with same session id detected" + "  Userd ID:  " +  userID);
	                        /*
	                        We redirect the user to a page which alerts him as well as gives him the option to destroy the 
	                        mulitple sessions if he does not trust them
	                        */

                       		RequestDispatcher rd =
          			        request.getRequestDispatcher("/Home/multipleUsers");
           			        rd.forward(request, response);
	                    }		        
		      }		      
		      st.close();
		      conn.close();		
		} catch (SQLException | NamingException e) {
			 logger.error("cannot search database. check query" + e.toString() );
		}
		
		doGet(request, response);
	}	

	
protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	response.getWriter().append("Served at: ").append(request.getContextPath()).append(" - OWASP Knowledge Base Code Examples");
}

}
/*
the only thing left to do now is to update your track_sessions table by inserting
the ipadress, sessionID and userID if you want to accept the other sessions as valid.
Otherwise the user just has to terminate the current session in order to lock out the
other sessions.
*/
	