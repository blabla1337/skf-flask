
Identifier-based authorization
-------

**Description:**
An application uses parameters in order to process data. These parameters can also be used to asign certain roles and retrieve 
content corresponding with those parameters. imagine the following example:

www.target.com/index.php?loggedin=user

In this situation the application wil get content and subscribe user roles corresponding to the user parameter

www.target.com/index.php?loggedin=admin

In this situation the application wil get content and subscribe user roles corresponding to the admin parameter.


**Solution:**
Whenever you are checking whether a user is restricted to review certain data the acces restrictions should be proccessed serverside.

The userID could be stored inside of a session variable on login and should be used to retrieve userdata from the database.

	