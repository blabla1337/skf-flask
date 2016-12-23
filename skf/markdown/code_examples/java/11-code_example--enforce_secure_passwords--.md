
Enforce Secure Password
------------------------

***Example:***

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

package com.edw;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.log4j.Logger;

public class passwordcheck {
	
	final static Logger logger = Logger.getLogger(sessionhijack.class);
	
	public boolean checkPassword(String password)
    {
		
		String error = "";
        boolean complete = true;
        /*
        Here we define the minimal expexted value's for your password.
        The password must at least contain a Capital letter, a normal letter, a special character
        a number and must be at least 8 characters long
        */
        
        String[] pattern = { "[0-9]", "[A-Z]", "[a-z]" };
       
        // Create a Pattern object
        // Now create matcher object.
        
         for (String vaildation : pattern )
         {
        	 
    	  // Create a Pattern object
   	      Pattern r = Pattern.compile(vaildation);
   	      // Now create matcher object.
   	      Matcher m = r.matcher(password);
	      if (!m.find()) {	
	    	  error = "You did not enter a valid password";
              complete = false;  
	      }		
         }
          	 /*
             Also very important is the fact that you have to take into consideration that
             Password1! is a valid password according to password standards. This however is not the case since
             this password is included in almost every dictionairy attack system. So we have to prevent 
             the user from using these weak passwords, this we do by defining these bad passwords in a text 
             file and compare the user's password with the bad passwords defined in the text file.
             */
             try {
             BufferedReader in = new BufferedReader(new FileReader("C:\\Users\\Public\\xml\\test.txt"));
             String[] strTemp = null ;
             String line;
             while((line = in.readLine()) != null)
             {
                
            	strTemp = line.split(",");
             }
             
             for (String value : strTemp)
             {	 
            	 if (value == password)
                 {
                     error = "Your password was a bad password!";
                     complete = false;
                 }          
             }
             
             in.close();
             }
             catch(IOException e) {
            	 logger.error(e.toString());
             }
         
         //The last step is checking the password length to see if it is 8 characters or bigger
         if (password.length() < 8)
         {
             error = "The password was to short";
             complete = false;

         }

         if (complete == true)
         {
             //Do further operation
             return true;
         }
         else
         {
             return false;
         }
    }

}

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
