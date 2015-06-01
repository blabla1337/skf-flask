
Input validation
-------

**Description:**

To ensure that the application is robust against all forms of input data, this data should 
be sanitised server-side since an attacker could otherwise easy bypass these checks with 
an intercepting proxy.


**Solution:**

All input validation and encoding-routines should be implemented on the server-side 
outside the reach of an attacker. Just as with the input rejection you should make sure that
after validating the userinput, whenever the input is bad it actually rejects, sanitises 
or formats your user-input into not malicious data. 

you must also keep track of the users movements by adding an audit trail as wel as an counter for
tracking the number of his violations(submitting bad input) in your input validation class. 
You should enforce a lockout whenever a unreasonable number of violations are detected 
by your application in order to protect it from attackers.
	