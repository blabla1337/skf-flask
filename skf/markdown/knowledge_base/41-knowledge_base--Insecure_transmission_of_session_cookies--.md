
Insecure transmission of session cookies
-------

**Description:**

If the session cookies are sent over an unencrypted connection, 
they should be withdrawn immediately. 
These cookies are not to be trusted anymore as a hacker may have captured their values.


**Solution:**

Session cookies that are used to authenticate the user should always set on a 
secure connection.
	