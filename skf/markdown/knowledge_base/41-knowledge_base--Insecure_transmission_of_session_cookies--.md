
Insecure transmission of session cookies
-------

**Description:**

If the session cookies are sent over an unencrypted connection, 
they should be withdrawn immediately. 
These cookies are not to be trusted anymore as a hacker may have captured their values.


**Solution:**

Session cookies that are used to authenticate the user should always be set on a 
secure connection. 

In order to achieve this you should set the "secure" flag on your session cookie
to make sure your application in any circumstance does not send this cookie over non
HTTPS connections. 
	
Recommended knowledge base item:
- Session management