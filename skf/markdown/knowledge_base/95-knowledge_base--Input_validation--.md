
Input validation
-------

**Description:**

To ensure that the application is robust against all forms of input data, this data should 
be sanitised server-side since an attacker could otherwise easy bypass these checks with 
an intercepting proxy.


**Solution:**

All input validation and encoding-routines should be implemented on the server-side 
outside the reach of an attacker.

	