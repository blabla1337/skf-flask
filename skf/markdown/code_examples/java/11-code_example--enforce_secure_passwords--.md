
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

public class PasswordCheck {
	
	final static Logger logger = Logger.getLogger(PasswordCheck.class);
	
	public boolean checkPassword(String password)
    {
		
		String error = "";
        boolean complete = true;
		
        /*
        for example here we define the expexted value's for your password.
		
		^                 # start-of-string
		(?=.*[0-9])       # a digit must occur at least once
		(?=.*[a-z])       # a lower case letter must occur at least once
		(?=.*[A-Z])       # an upper case letter must occur at least once
		(?=.*[@#$%^&+=])  # a special character must occur at least once
		(?=\S+$)          # no whitespace allowed in the entire string
		.{8,}             # anything, at least eight places though
		$                 # end-of-string
        */
        
        String vaildation = "^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])(?=\S+$).{8,}$";    

    	  // Create a Pattern object
   	      Pattern reg = Pattern.compile(vaildation);
   	      // Now create matcher object.
   	      Matcher match = reg.matcher(password);
	      if (!match.find()) {	
	    	  error = "You did not enter a valid password";
              complete = false;  
	      }		
          	 /*
             Also we have to take into consideration that Password1! is a valid password according to password standards. This however is not the case since this password is included in almost every dictionairy attack mechanisms. So we have to prevent the user from using these weak passwords. In such case we will define these bad passwords in a text 
             file in order to compare the user's password with the list of bad passwords inside that file.
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
            	 if (value.equals(password))
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

         if (complete)
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
