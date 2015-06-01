
Input rejection
-------

**Description:**

Whenever the application detects malicious or unexpected user-input you want to make sure 
the application actual rejects the submitted user-input rather than directly process it. 


**Solution:**

Verify that the application actually rejects, sanitises or format your user-input into not 
malicious data. 

you must also keep track of the users movements by adding an audit trail as wel as an counter for
tracking the number of his violations(submitting bad input) in your input validation class. 
You should enforce a lockout whenever a unreasonable number of violations are detected 
by your application in order to protect it from attackers.
 
	