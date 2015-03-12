
The crossdomain.xml should only contains trusted domains 
-------

**Description:**

The use of a crossdomain.xml file is required when the web application uses Flash. 
This file is used to set up restrictions for any other web servers using the 
flash application. If these are not set correctly, an attacker could exploit this to 
execute targeted attacks against the users of the web application.
  

**Solution:**

Always make sure the crossdomain.xml only contains trusted domains.

	