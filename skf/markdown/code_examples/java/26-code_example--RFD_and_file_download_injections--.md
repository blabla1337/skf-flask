
RFD and file download injections
---------------------------------


***Example:***

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

//REFLECTED – some input is reflected to the response body. --> shell commands
//FILE – attacker can tamper the filename.
//DOWNLOAD – the response is downloaded.


package com.edw;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.time.LocalDateTime;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;
import javax.sql.DataSource;

/**
 * SERVLET implementation class DownLoadFiles
 */
@WebServlet("/DownLoadFiles")
public class DownLoadFiles extends HttpServlet {
	private static final long serialVersionUID = 1L;
    private AuditLog Log = new AuditLog(); 
    private final static Logger logger = Logger.getLogger(DownLoadFiles.class.getCanonicalName());
    inputvalidation validate = new inputvalidation();
    whitelist whitelist = new whitelist();
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public DownLoadFiles() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.getWriter().append("Served at: ").append(request.getContextPath());
	}

	/**
	 * @throws IOException 
	 * @throws ServletException 
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException
	{
		String filename = request.getParameter("filename");
		String userID = request.getSession().getAttribute("userID").toString(); 
        
		String action = downloadUserFiles(filename, userID, request, response);
		
		if (action.equals("terminate"))
		{
			 request.getSession().invalidate();
	    	 request.setAttribute("msg","Session terminated! file has not been downloaded");
	    	 request.getRequestDispatcher("/login.jsp").forward(request, response);
		     return;
		}
		if (action.equals("validation failed"))
		{
			 request.setAttribute("msg","FAIL! file has not been downloaded");	
	    	 RequestDispatcher dd = request.getRequestDispatcher("/FileDownload.jsp");
	    	 dd.forward(request, response);			    
		     return;
		}
		if (action.equals("block"))
		{
			 request.setAttribute("msg","Access Blocked! file has not been downloaded");
	    	 request.getRequestDispatcher("/login.jsp").forward(request, response);
		     return;	
		}
		if (action.equals("Validated Successfully"))
		{
			request.setAttribute("msg","SUCCESS! file downloaded");
	    	 request.getRequestDispatcher("/FileDownload.jsp").forward(request, response);
		     return;
		}
		doGet(request, response);
	}
	
	
	public String downloadUserFiles(String file, String userID, HttpServletRequest request, HttpServletResponse response){
		
		response.setContentType("text/html;charset=UTF-8");
        String action = ""; 
        boolean proceed = false ;
        String mimetype = "";
		 // Create path components to save the file
        // The location of stored files should always be outside of your root
      
        final String path = request.getParameter("destination");
     	final File f = new File(path);
        Part filePart = null;
		try {
			filePart = request.getPart(f.toString());
		} catch (IOException | ServletException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
        //We get the filename for doing different types of tests on it
        final String fileName = getFileName(filePart);
      
        /*
        First we check if the value is alphanumeric only to prevent uploading out of intended directory, 
        as well as other injections
        */
        
        if (validate.validateInput(userID, fileName, "alphanummeric", "validation failed",request.getRemoteAddr(),"HIGH") == "validation failed")
        {
           proceed = false;
           action = "validation failed";
        }
        
        else if (validate.validateInput(userID, fileName, "alphanummeric", "Session Termination",request.getRemoteAddr(),"HIGH") == "terminate")
        {
        	proceed = false;
        	action = "terminate";
        }   
        
        else if (validate.validateInput(userID, fileName, "alphanummeric", "Block access",request.getRemoteAddr(),"HIGH") == "block")
        {
        	proceed = false;
        	action = "block";
        }  
        else 
        {
        	Log.SetLog(userID, "Validated Successfully" , "SUCCESS", LocalDateTime.now(),request.getRemoteAddr(),  "");
        	action = "Validated Successfully";
        	proceed = true;
        }
        
        if (proceed == true)
        {
        	 //Here we connect to the database by means of a connection string as configured in the web.xml and /META-INF/context.xml 
			Connection conn = null;
		    try {
					
			Context initContext = new InitialContext();
			Context webContext  = (Context)initContext.lookup("java:/comp/env");
			DataSource ds = (DataSource)webContext.lookup("jdbc/myJdbc");
			conn = ds.getConnection();	

			  //Here we select the number of counts from aggregate column in order to verify the number of connections:
		      String query = "SELECT * FROM downloads WHERE userID=?";
		   
		      PreparedStatement st = conn.prepareStatement(query);
		      st.setString(1, userID);
		      
		      
		      // execute the query, and get a java result set
		      //We bind the parameter in order to prevent SQL injections

		      ResultSet rs = st.executeQuery();
		      
		      while (rs.next())
		      {
		    	  mimetype   = rs.getString("mimeType");
		
		      }
		      st.close();
	          conn.close();
			} catch (SQLException | NamingException e) {
				 logger.log(Level.SEVERE, "cannot update database. check query = {0}", e.toString());

			}	  
        	
        }
        
        if (fileName != null)
        {
        	
        	/*
            We also define the mime-type per download file.
            This is because whenever a user can only download images it is not necessary to set
            an uncommon content-type header for it.
            NOTE: These mime-types should not be stored based upon the mime-type which was send 
            the response header when the user uploaded the file. This value can be easily 
            manipulated with an intercepting PROXY. You should get the mime-type from the file
            itself after it was stored on the server.
            */
        	response.reset();
        	response.setContentType(mimetype);
        	response.addHeader("Cache-Control", "no-cache");
        	response.addHeader("Content-Disposition", "attachment; filename=" + fileName + ";");
        	
        	OutputStream out;
			try {
				out = response.getOutputStream();
			
        	FileInputStream in = new FileInputStream(fileName);
        	byte[] buffer = new byte[4096];
        	int length;
        	while ((length = in.read(buffer)) > 0){
        	    out.write(buffer, 0, length);
        	}
        	in.close();
        	out.flush();
        	
			} catch (IOException e) {
				 logger.log(Level.SEVERE, "Cannot download file = {0}", e.toString());
			
			}
          
        }
        else if (fileName == null)
        {
        	action = "empty";
        }
        
      return action ; 
	}
	
	 public void fixedDownloads(String file, String download, HttpServletResponse response)
     {
		 
		 /*
         The second example is for whenever you are providing users with fixed downloads
         such as manuals etc. We do not only check if the file just exists, because that would
         allow an attacker to also download important other files from your server, so instead
         we white-list them.
         */
		  if (whitelist.whitelisting(file, download) != false)
          {
			  
			    response.reset();
	        	response.setContentType("text/plain");
	        	response.addHeader("Cache-Control", "no-cache");
	        	response.addHeader("Content-Disposition", "attachment; filename=" + file + ";");
	        	
	        	OutputStream out;
				try {
				
				out = response.getOutputStream();
			
	        	FileInputStream in = new FileInputStream(file);
	        	byte[] buffer = new byte[4096];
	        	int length;
	        	while ((length = in.read(buffer)) > 0){
	        	    out.write(buffer, 0, length);
	        	}
	        	in.close();
	        	out.flush();
				} catch (IOException e) {
					 logger.log(Level.SEVERE, "Cannot download file = {0}", e.toString());
			
				}
			  
          }
		 
		 
     }
	 
	 
	 private String getFileName(final Part part)
	 {
	         final String partHeader = part.getHeader("content-disposition");
	         logger.log(Level.INFO, "Part Header = {0}", partHeader);
	         
	         for (String content : part.getHeader("content-disposition").split(";"))
	         {
	             if (content.trim().startsWith("filename"))
	             {
	                 return content.substring(content.indexOf('=') + 1).trim().replace("\"", "");
	             }
	         }
	         
	         return null;
	 }   

}

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
