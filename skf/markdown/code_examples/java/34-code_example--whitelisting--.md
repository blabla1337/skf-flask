Whitelisting 
-------------

***Example:***

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

package com.edw;


import org.apache.log4j.Logger;

public class Whitelist
{
	
	final static Logger logger = Logger.getLogger(Whitelist.class);

	
	public boolean whitelisting(String allowed, String input)
	
	{
		 /*
        Here we define a white list of pages we want the user to be allowed to be redirected to, all 
        patterns are terminated whenever they not comply with the predefined white list
        */
		
		String[] pattern = allowed.split(",");
		
		 //For validation if the file returned true
		boolean validated = false;
		
		 //To catch the user submitting evil requests we count the number of times the for loop hits false
        int count = 0;
        int countArray = 0;
		         
        for( int i = 0; i < pattern.length; i++)
        {
            String item = pattern[i];
            
          //If filename is equal to the predefined items
            if ( input == item)
            {
            	validated = true ; 
               	count = -1;
            }
            
            //Here we increase the counts, if they are equal we know the function did not hit a valid filename
            count++;
            countArray++;
        }
		 
        if (countArray == count)
        {
        	
        	//this breach has to be reported into the log files
        	validated = false;
        	logger.info("Audit log message!" + "FAIL" + "HIGH");

        	
        }
        
		
		return validated;
		
	}
	
}

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
