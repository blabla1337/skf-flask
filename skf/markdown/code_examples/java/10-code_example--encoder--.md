
Encoder (SQL - ESAPI)
-----------

***Example:***

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

package com.edw;

import java.time.LocalDateTime;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import org.owasp.esapi.ESAPI;
import org.owasp.esapi.codecs.MySQLCodec;

public class Encoding {
	
	AuditLog Log = new AuditLog(); 
	
	public String encoder(String input , String allowed, String user_id)
	{	
		/*
        We can specify also special characters which allowed in order to keep
        track of any unwanted special characters
        
        Example :
        
        To keep malicious inputs contained, any inputs written to the database need to be encoded.
		SQL encoding: ' OR 1=1 --' is encoded to \' OR 1\=1 \-\-\'
		
        */
		  String pattern = "^[a-zA-Z0-9" + allowed + "]+$";
	      // Create a Pattern object
	      Pattern reg = Pattern.compile(pattern);
	      // Now create matcher object.
	      Matcher match = reg.matcher(input);
	      if (!match.find()) {	
				Log.SetLog(user_id, "Illegal characters", "FAIL", LocalDateTime.now(),  "HIGH");
	      }		
	    //We return the user input encoded	      
		return ESAPI.encoder().encodeForSQL(new MySQLCodec(MySQLCodec.MYSQL_MODE), input);
	}
}

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~