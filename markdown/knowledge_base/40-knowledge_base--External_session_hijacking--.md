
External session hijacking
-------

**Description:**

When an attacker obtains a users session cookie, then he could steal the identity of the user which the session cookie belonged to.


**Solution:**

As soon as a session is set for an authenticated user, the server should keep track of the IP adress in which the user used when he started the session. When the server discovers a change in IP adress, for instance when an attacker hijacks an users session. The server then should deny access, destroy the session and redirect the &#34;hijacker&#34; to the login page.

	