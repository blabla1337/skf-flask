
Open forward &amp; Open redirects
-------

**Description:**

An open forward is an application that takes a parameter and forwards a user to another 
part of the application without any validation or access control checks. 
This may allow an attacker to bypass access control checks, especially those enforced 
externally, such as by a web server. 



**Solution:**

Use a whitelisting method for determining where the user should be redirected towards.

	