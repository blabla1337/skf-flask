# File Upload 
-------

## Example:


In this example we show the steps that must be taken in order to upload a file securely. The main steps are input validation ,file extension checks and mime type checks. 
the following code snipet shows the jsp page that performs the post action to upload a certain file to destination 


<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
    <head>
        <title>File Upload</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    </head>
    <body>
        <form method="post" action="FileUpload" enctype="multipart/form-data" >
            File:
            <input type="file" name="file" id="file" /> <br/>
            Destination:
            <input type="text" value="C:\Users\someuser\Desktop\test" name="destination"/>
            </br>
            <input type="submit" value="Upload" name="upload" id="upload" />
        </form>
        <%
		String message =  " "; 
        message = (String) request.getAttribute("msg");
        if (message == null)
        {
        	message = " ";
        }
		out.println(" " + message);
	    %> 
    </body>
</html>


the following code snipet performs the file uploading functionality from the post action performed at the jsp page showed above



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
import org.apache.log4j.Logger;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;
import com.Lib.AuditLog;
import com.Lib.WinRegistry;
import com.Lib.InputValidation;

import org.apache.commons.io.FilenameUtils;

@MultipartConfig
public final class FileUpload extends HttpServlet {
	
    /**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	final static Logger logger = Logger.getLogger(FileUpload.class);
	private AuditLog Log = new AuditLog(); 
    InputValidation validate = new InputValidation();

    //We check for form submit
  
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException
    {
        response.setContentType("text/html;charset=UTF-8");
        String userID = request.getSession().getAttribute("userID");
        boolean continueFunction = true;
        boolean sessionTermination = false;
        boolean blockAccess = false ;
        
        // Create path components to save the file
        // The location of stored files should always be outside of your root
        
        // the destination path used to store the file gotten from the POST parameter
		
        final String path = request.getParameter("destination");
     	final File f = new File(path);
        final Part filePart = request.getPart("file");
        //We get the filename for doing different types of tests on it
        final String fileName = getFileName(filePart);
      
        /*
        First we check if the value is alphanummeric only to prevent uploading out of intended directory, 
        as wel as other injections
        */
        
        if (validate.validateInput(userID, fileName, "alphanummeric", "validation failed",request.getRemoteAddr(),"HIGH").equals("validation failed"))
        {
           continueFunction = false;
        }
        
        else if (validate.validateInput(userID, fileName, "alphanummeric", "Session Termination",request.getRemoteAddr(),"HIGH").equals("terminate"))
        {
           request.getSession().invalidate();
           continueFunction = false;
           sessionTermination=true;
        }   
        
        else if (validate.validateInput(userID, fileName, "alphanummeric", "Block access",request.getRemoteAddr(),"HIGH").equals("block"))
        {
           continueFunction = false;
           blockAccess=true;
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
        
        String  fileExtension = FilenameUtils.getExtension(fileName);

        if (!fileExtension.equals("jpg") && !fileExtension.equals("png") )
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
                       
			logger.info("File" + fileName + "has beeng uploaded to" + path); 
            
        } catch (FileNotFoundException fne) {

			  logger.error("Problems during file upload. Error:" + fne.toString());
      	
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
			logger.error("Problems during file upload. Error: " + e.toString());
		}
        	
        	
        	String mimeType = "application/unknown";
			try {
				mimeType = WinRegistry.readString(WinRegistry.HKEY_LOCAL_MACHINE, "SOFTWARE\\Classes\\"+key, "Content Type");
			} catch (IllegalArgumentException | IllegalAccessException | InvocationTargetException e) {
				logger.error("Problems reading the extension value on Windows registry. Error: " + e.toString());
			}

  
			if (mimeType == null || !mimeType.equals("image/jpeg"))
        	   {
        		  //If the mimetype is not valid we delete the file from the system.
        		  f.delete();
        		  continueFunction = false;
        		
        	   }
			
			  
     
			    if (continueFunction == false && sessionTermination == false && blockAccess == false)
		        {    
			    	 request.setAttribute("msg","FAIL! file has not been uploaded");	
			    	 RequestDispatcher dd = request.getRequestDispatcher("/FileUpload.jsp");
			    	 dd.forward(request, response);			    
				     return;		   
		        }
			      
			    if (continueFunction == true && sessionTermination == false && blockAccess == false)
			    {
			    	 request.setAttribute("msg","SUCCESS! file uploaded");
			    	 request.getRequestDispatcher("/FileUpload.jsp").forward(request, response);
				     return;
			    	
			    }      
			    
			    if (continueFunction == false && sessionTermination == false && blockAccess == true)
		        {  
			    	 request.setAttribute("msg","Access Blocked!");
			    	 request.getRequestDispatcher("/error.jsp").forward(request, response);
				     return;
			    	
		        }
			    
			    if (continueFunction == false && sessionTermination == true && blockAccess == false)
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
		logger.info("Part Header = " + partHeader)
        
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




