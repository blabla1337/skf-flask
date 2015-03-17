
Absolute session time-out
-------

**Description:**

All sessions should implement an absolute timeout, regardless of session activity. 
This timeout defines the maximum amount of time a session can be active, 
closing and invalidating the session upon the defined absolute period since the given 
session was initially created by the web application. After invalidating the session, 
the user is forced to (re)authenticate again in the web application and establish 
a new session. The absolute session limits the amount of time an attacker can use a 
hijacked session and impersonate the victim user. 


**Solution:**

Always ensure that sessions absolute time-out in order to decrease a hackers 
attack vector.

	