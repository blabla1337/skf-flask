# Open Forwards and Redirects 
-------

## Example:


/*
When using forwards & redirects you should make sure the URL is being explicitly 
declared in the code and cannot be manipulated by an attacker like:
*/

//response.Redirect("/login");


/*
Generally you should avoid getting input into the redirect which could contain
user-input by any means. if for any reason this may not be feasible than you 
should make a WhiteList input validation for the redirect like so:
*/

package com.edw;

public class OpenForwards {

	public boolean openForwards(String redirect)
    {
        WhiteList listMe = new WhiteList();

        boolean validated = true;

        //For more information about white-listing see the "WhiteListing" code example:
        if (listMe.WhiteListing("page1,page2,page3", redirect) == false) { validated = false; }

        //return the value back to the servlet in order to handle redirections. 
		//if the variable validate is true then it will redirect
		
        return validated; 
     
    }
	
}
