File Upload 
-------------


***Example:***

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example we show the steps that must be taken in order to upload a file securely. The main steps are input validation 
,file extension checks and mime type checks. 

package com.edw;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.lang.reflect.InvocationTargetException;
import java.time.LocalDateTime;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;

import org.apache.commons.io.FilenameUtils;

@MultipartConfig
public class FileUpload extends HttpServlet {
	
    /**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private final static Logger LOGGER = Logger.getLogger(FileUpload.class.getCanonicalName());
	private AuditLog Log = new AuditLog(); 
    inputvalidation validate = new inputvalidation();

    //We check for form submit
  
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException
    {
        response.setContentType("text/html;charset=UTF-8");
        String userID = request.getSession().getAttribute("userID");
        boolean continueFunction = true;
        boolean sessiontermination = false;
        boolean blockaccess = false ;
        
        // Create path components to save the file
        // The location of stored files should always be outside of your root
        
        
        final String path = request.getParameter("destination");
     	final File f = new File(path);
        final Part filePart = request.getPart("file");
        //We get the filename for doing different types of tests on it
        final String fileName = getFileName(filePart);
      
        /*
        First we check if the value is alphanummeric only to prevent uploading out of intended directory, 
        as wel as other injections
        */
        
        if (validate.validateInput(userID, fileName, "alphanummeric", "validation failed",request.getRemoteAddr(),"HIGH") == "validation failed")
        {
           continueFunction = false;
        }
        
        else if (validate.validateInput(userID, fileName, "alphanummeric", "Session Termination",request.getRemoteAddr(),"HIGH") == "terminate")
        {
           request.getSession().invalidate();
           continueFunction = false;
           sessiontermination=true;
        }   
        
        else if (validate.validateInput(userID, fileName, "alphanummeric", "Block access",request.getRemoteAddr(),"HIGH") == "block")
        {
           continueFunction = false;
           blockaccess=true;
        }  
        else 
        {
        	Log.SetLog(userID, "Validated Successfully" , "SUCCESS", LocalDateTime.now(),request.getRemoteAddr(),  ""); 
        	
        }
        
        /*
        The next step would be checking if the file contains the right extension in order to prevent
        a user from uploading files which could be used to harm your system. in this example 
        we check if the last extension found in the file name is a jpg or a png. whenever
        an application just regexes for the extension an attacker could
        bypass the check by uploading an file like: "filename.jpg.php".
        */       
        
        String  StrSpli = FilenameUtils.getExtension(fileName);

        if (!StrSpli.equals("jpg") && !StrSpli.equals("png") )
        {
            continueFunction = false;
     
        }

        /*
         If the file came through all the different checks, it is time to upload the file to your system. 
         */
        if (continueFunction == true)
        {       
        OutputStream out = null;
        InputStream filecontent = null;

        //start uploading the file
        try {
            out = new FileOutputStream(new File(path + File.separator + fileName));
            filecontent = filePart.getInputStream();

            int read = 0;
            final byte[] bytes = new byte[1024];

            while ((read = filecontent.read(bytes)) != -1) {
                out.write(bytes, 0, read);
            }
                       
            LOGGER.log(Level.ALL, "File {0} being uploaded to {1}" ,  new Object[]{fileName, path});
            
        } catch (FileNotFoundException fne) {

          	 LOGGER.log(Level.SEVERE, "Problems during file upload. Error: {0}", new Object[]{fne.getMessage()});
      	
        } finally {
            if (out != null) {
                out.close();
            }
            if (filecontent != null) {
                filecontent.close();
            }
         }
      
        }
        
        /*
        Now we check the uploaded file for the right mime-type
        We do this after the upload instead of checking the content type header since that header 
        can easily manipulated by an attacker. 
         */
                
        List<String> ls = null;
        String key = null;
		try {
			ls = WinRegistry.readStringSubKeys(WinRegistry.HKEY_LOCAL_MACHINE,"SOFTWARE\\Classes\\");
			key = ls.stream().filter(st -> st.matches("."+StrSpli)).findAny().orElse(null);
			
		} catch (IllegalArgumentException | IllegalAccessException | InvocationTargetException e) {
			LOGGER.log(Level.SEVERE, "Problems reading the extension key on Windows registry. Error: {0}", new Object[]{e.getMessage()});
			
		}
        	
        	
        	String mimeType = "application/unknown";
			try {
				mimeType = WinRegistry.readString(WinRegistry.HKEY_LOCAL_MACHINE, "SOFTWARE\\Classes\\"+key, "Content Type");
			} catch (IllegalArgumentException | IllegalAccessException | InvocationTargetException e) {
				// TODO Auto-generated catch block
				LOGGER.log(Level.SEVERE, "Problems reading the extension value on Windows registry. Error: {0}", new Object[]{e.getMessage()});
			}

  
			if (mimeType == null || !mimeType.equals("image/jpeg"))
        	   {
        		  //If the mimetype is not valid we delete the file from the system.
        		  f.delete();
        		  continueFunction = false;
        		
        	   }
			
			  
     
			    if (continueFunction == false && sessiontermination == false && blockaccess == false)
		        {    
			    	 request.setAttribute("msg","FAIL! file has not been uploaded");	
			    	 RequestDispatcher dd = request.getRequestDispatcher("/FileUpload.jsp");
			    	 dd.forward(request, response);			    
				     return;		   
		        }
			      
			    if (continueFunction == true && sessiontermination == false && blockaccess == false)
			    {
			    	 request.setAttribute("msg","SUCCESS! file uploaded");
			    	 request.getRequestDispatcher("/FileUpload.jsp").forward(request, response);
				     return;
			    	
			    }      
			    
			    if (continueFunction == false && sessiontermination == false && blockaccess == true)
		        {  
			    	 request.setAttribute("msg","Access Blocked!");
			    	 request.getRequestDispatcher("/error.jsp").forward(request, response);
				     return;
			    	
		        }
			    
			    if (continueFunction == false && sessiontermination == true && blockaccess == false)
		        {  
			    	 request.getSession().invalidate();
			    	 request.setAttribute("msg","Session terminated!");
			    	 request.getRequestDispatcher("/error.jsp").forward(request, response);
				     return;
			    	
		        }
			    
    }



@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

		super.doGet(req, resp);
	}

/*
reading from headers 
...
POST /fileupload/upload HTTP/1.1
Host: localhost:8080
Content-Type: multipart/form-data; 
boundary=---------------------------263081694432439
Content-Length: 441
-----------------------------263081694432439
Content-Disposition: form-data; name="file"; filename="sample.txt"
Content-Type: text/plain
[ ..... ]
*/

private String getFileName(final Part part)
{
        final String partHeader = part.getHeader("content-disposition");
        LOGGER.log(Level.INFO, "Part Header = {0}", partHeader);
        
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


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

