
Dynamic scripting injection
-------

**Description:**

When user input is used to evaluate scripting code then this could introduce 
high security risks. If the input is not properly escaped an attacker can inject his own 
script code and gain access to the server.


**Solution:**

Do not use direct user-input in the dynamic scripting function.
	