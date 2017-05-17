Login Functionality 
--------------------

***Example:***

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


package com.edw;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.UUID;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.servlet.ServletException;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.sql.DataSource;

import org.apache.log4j.Logger;

public class Login extends HttpServlet{

	 final static Logger logger = Logger.getLogger(Login.class);
	 public String password ;
	 public String username;
	 public int userID;
	 public String salt;
	 public String access ;
	 public int privilege;	 

	  //First we include the audit log class.
	  auditlogs Log = new auditlogs();
		
	  //Second we include the password hash.
	  hashing hash = new hashing();

	  //Third we include the random password/token class.
	  randomizer CSRF = new randomizer();
	    
	  //Last we include the random inputvalidation class.
	  inputvalidation validate = new inputvalidation();
	 	   
	 /**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

    	username = req.getParameter("username");
		
    	this.checkSession(req, resp);
    	
        String passwordHash = "";
        String userId = "";

        //we also validate the username input, if it was bad we empty the string:
        if (validate.validateInput(username, "alphanummeric", "Error in username", "LOW", "0") != true) { username = ""; }
     
    	//Here we connect to the database by means of a connection string as configured in the web.xml 
        Connection conn = null;
	    try {
			
		 Context initContext = new InitialContext();
		 Context webContext  = (Context)initContext.lookup("java:/comp/env");
		 DataSource ds = (DataSource)webContext.lookup("jdbc/myJdbc");
		 conn = ds.getConnection();	

		 //Here we select the user from the users table
	      String query = "SELECT * from users WHERE username = ?";
	   
	      PreparedStatement st = conn.prepareStatement(query);
	      st.setString(1, username);
	      
	      //execute the query, and get a java resultset
	      //We bind the parameter in order to prevent sql injections

	      ResultSet rs = st.executeQuery();
	      
	      while (rs.next())
	      {
	    	  username   = rs.getString("username");
	    	  passwordHash = rs.getString("password");
              salt = rs.getString("salt");
              userId = rs.getString("userID");
	      }
	      
	      st.close();
	      conn.close();
	    
		} catch (SQLException | NamingException e) {
			 logger.error("cannot search database. check query" + e.toString() );
		}

	    /*
        We validate the password see "Password storage(salting stretching hashing)" in the code examples
        for more detailed information:
        */
        if (hash.Validate(passwordHash, salt, password) == true)
        {
        	/*
            This is is to prevent session fixation, after login we create a new cookie which
            we then use to authenticate. This value can not be fixated since it is set after 
            login.

            create a new UUID and save into the session:
            */
        	 UUID uuid = UUID.randomUUID();
        	
        	 String randomUUIDString = uuid.toString();
        	
        	 req.getSession().setAttribute("AuthToken", randomUUIDString);  
        	
        	// now create a new cookie with this UUID value
        	 Cookie newCookie = new Cookie("AuthToken", randomUUIDString);        	 
        	 resp.addCookie(newCookie);
        	 
        	//the connection has to be reported into the log files
             Log.SetLog("", "", "login was OK!", "SUCCESS", "NULL");
             
             /*
             Now we create a random value for our CSRF tokens. See "Random password token generation" in
             the code examples for more detailed information:
             */
             String CSRftoken = CSRF.generate(25);
             
             //Set an accessor session.
             req.getSession().setAttribute("CSRF", CSRftoken);  
             
             /*
             Put id in a session for query identifier based authentication
             See "identifier based authentication" code example for more information
              */
             req.getSession().setAttribute("userID", userId);

                 
        }
        else
        {
            //the connection has to be reported into the log files
            Log.SetLog("", "null", "Login failed!", "FAIL", "NULL");
         
            
            req.setAttribute("msg","Session terminated!");
	    	req.getRequestDispatcher("/login.jsp").forward(req, resp);
		    return;
        }	
		
		super.doGet(req, resp);
	}

	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		// TODO Auto-generated method stub
		super.doPost(req, resp);
	}

    //In this method we do a check if the sessions are ok
    public void checkSession(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException
    {
    	
    	 Cookie cookie = null;
   	  	 Cookie[] cookies = null;
         // Get an array of Cookies associated with this domain
         cookies = req.getCookies();
         
         String authtoken = " "; 
         for (int i = 0; i < cookies.length; i++){
             cookie = cookies[i];
             
         if (cookie.getName().equals("AuthToken"))
         {
        	 authtoken = cookie.getName(); 
         }
         
    	//We use this try catch for whenever the cookie is dropped
         try
         {
            //Check sessions and cookies to see if they match
        	if (!req.getSession().getAttribute("AuthToken").equals(authtoken) || req.getSession().getAttribute("AuthToken") != "access")
        	{
        		req.setAttribute("msg","Session terminated!");
     	    	req.getRequestDispatcher("/login.jsp").forward(req, resp);
     		    return;
        	}
         }

        catch (Exception e)
        {
        		logger.error(e.toString());
          		req.getSession().removeAttribute("Authenticated");
        		req.getSession().invalidate();
    	    	req.getRequestDispatcher("/login.jsp").forward(req, resp);
    		    return;       
        }
    }    
 }
}

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
