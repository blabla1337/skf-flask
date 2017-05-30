Directory Path traversal 
-------------------------

***Example:***

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`

package com.edw;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import com.edw.InputValidation;
import com.edw.WhiteList;
import org.apache.log4j.Logger;

public class Rewrite extends HttpServlet
{

	private static final long serialVersionUID = 1L;
    private File getFile;
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Rewrite() {
        super();
    }
	
	final static Logger logger = Logger.getLogger(Rewrite.class);
	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException 
	{
			InputValidation validate = new InputValidation();
			WhiteList listme = new WhiteList();

			/*
            First, we want to filter the filenames for expected values. For this example we use only use 0-9
            Whenever the values are tampered with, we can assume an attacker is trying to inject malicious input.           
            */
            boolean validated = true;

            //see the "input validation" code example for more detailed information about this function
			
			final boolean validInput = validate.validateInput(getFile.toString(), "nummeric", "Failed to get file", "HIGH");
			
			if (!validInput) { 
				validated = false; 
			}
            /*
            see the "WhiteListing" code example for more detailed information about this function
            Let's assume there are three files named 1,2,3
            */

            if (listme.WhiteListing("1,2,3", getFile.toString()) == false) { validated = false; }

            //Only if the pattern was true we allow the variable into the streamreader function
            if (validated)
            {
            	String canonicalPath = getFile.getCanonicalPath();
            	if (!canonicalPath.equals("C:\\....\\WEB-INF" + getFile)) 
            	{
            	   // Invalid file; handle error
            	}            	 
            	FileInputStream fis = new FileInputStream(canonicalPath);            	
            }         
            else
            {
            	logger.error("invalid userinput was detected!");              
            }
            doGet(request,response);
   
	}
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.getWriter().append("Served at: ").append(request.getContextPath()).append(" - OWASP Knowledge Base Code Examples");
	}

}

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
