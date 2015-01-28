
External session hijacking
-------


**Description:**

When an attacker obtains a users session cookie, then he could steal the identity of the user which the session cookie belonged to.


**Solution:**

As soon as a session is set for a authenticated user, the server should keep track of the ip adress in which the user used when he 
started the session. When the server discovers a change in ip adress, for instance when an attacker hijacks a users session. The server then
should deny access and redirect the "hijacker" to the login page.	