# Reauthentication 
-------

## Example:


	package com.edw;

	import java.io.IOException;
	import java.net.HttpCookie;
	import java.sql.Connection;
	import java.sql.PreparedStatement;
	import java.sql.ResultSet;
	import java.sql.SQLException;
	import java.time.LocalDateTime;

	import javax.naming.Context;
	import javax.naming.InitialContext;
	import javax.naming.NamingException;
	import javax.servlet.ServletException;
	import javax.servlet.annotation.WebServlet;
	import javax.servlet.http.Cookie;
	import javax.servlet.http.HttpServlet;
	import javax.servlet.http.HttpServletRequest;
	import javax.servlet.http.HttpServletResponse;
	import javax.sql.DataSource;
	import java.util.UUID;

	import org.apache.log4j.Logger;

	import com.ning.http.client.Request;

	/**
	* Servlet implementation class Reauth
	*/
	@WebServlet("/Reauth")
	public final class Reauth extends HttpServlet {
		private static final long serialVersionUID = 1L;
		private int userID; 
		private String username; 
		private String password; 
		private String access; 
		private String salt; 
		private int privilege; 
		private boolean loggedin = false;
		final static Logger logger = Logger.getLogger(Reauth.class);
		
		AuditLog Log = new AuditLog();

		//Second we include the password hash.
		Hashing hash = new Hashing();

		//Third we include the random password/token class.
		Randomizer CSRF = new Randomizer();
		
		/**
		* @see HttpServlet#HttpServlet()
		*/
		public Reauth() {
			super();
		}

		/**
		* @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
		*/
		protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
			response.getWriter().append("Served at: ").append(request.getContextPath());
		}

		/**
		* @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
		*/
		protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
			
			loggedin = reAuthentication(request,response);
			
			if (loggedin == false)
			{
				request.getSession().invalidate();
				request.getSession().setAttribute("Athenticated", "");
				
				Cookie cookie = null;
				Cookie[] cookies = null;
				// Get an array of Cookies associated with this domain
				cookies = request.getCookies();
					
				for (Cookie cookie2 : cookies) {
					cookie = cookie2;
						
					if (cookie.getName().equals("JSESSIONID"))
					{        	 
						cookie.setValue("");
					}         
					response.addCookie(null);
					request.setAttribute("msg","Session terminated!");
					request.getRequestDispatcher("/login.jsp").forward(request, response);
					return;
				}
			}
			doGet(request, response);
		}
		
		public boolean reAuthentication(HttpServletRequest request, HttpServletResponse response)
		{
			String passwordHash = "";
			//Here we connect to the database by means of a connection string as configured in the web.xml and /META-INF/context.xml 
			Connection conn = null;
			try {		
				Context initContext = new InitialContext();
				Context webContext  = (Context)initContext.lookup("java:/comp/env");
				DataSource ds = (DataSource)webContext.lookup("jdbc/myJdbc");
				conn = ds.getConnection();	

				//Here we select the number of counts from aggregate column in order to verify the number of connections:
				String query = "SELECT * from users WHERE userID = ?";
			
				PreparedStatement st = conn.prepareStatement(query);
				st.setInt(1, userID);
				
				// execute the query, and get a java result set
				//We bind the parameter in order to prevent SQL injections
				ResultSet rs = st.executeQuery();
				while (rs.next())
				{
					passwordHash  = rs.getString("password");
					salt = rs.getString("password");
				}
				
				st.close();
				conn.close();
			
			} catch (SQLException | NamingException e) {
				logger.error("cannot search database. check query" + e.toString() );
			}
			
			/*
			We validate the password see "Password storage(salting stretching Hashing)" in the code examples
			for more detailed information:
			*/
			if (hash.Validate(passwordHash, salt, password) == true)
			{
				//the connection has to be reported into the log files	
				Log.SetLog("Null", "login was OK!", "SUCCESS", LocalDateTime.now(), "NULL");

				/*
				This is is to prevent session fixation, after login we create a new cookie which
				we than use to authenticate. This value can not be fixated since it is set after 
				login.

				create a new UUID and save into the session:
				*/
		
				//All the random tokens will now be changed
				UUID uid = UUID.randomUUID();          
				String AuthToken = uid.toString();
				request.getSession().setAttribute("AuthToken", AuthToken);
				
				// now create a new cookie with this UUID value
				Cookie cookie = new Cookie("AuthToken",AuthToken);
				response.addCookie(cookie);

				/*
				Now we create a random value for our CSRF tokens. See "Random password/token generation" in
				the code examples for more detailed information:
				*/
				
				String CSRftoken = CSRF.generate(25);
				request.getSession().setAttribute("CSRF", CSRftoken);
				request.getSession().setAttribute("access", "Authenticated");

				loggedin = true;
			}else{
				//If things went wrong we destroy the entire session. see "logout" code example for more info:
				loggedin = false ;
			}
			return loggedin;
		}
	}
