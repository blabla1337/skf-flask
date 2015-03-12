
Session cookies without the HttpOnly flag
-------

**Description:**

The http-only flag is an option that can be set when creating a cookie. 
This flag ensures that the cookie can not be read or edited by javascript. 
This ensures that an attacker can not steal this cookie as a cross-site scripting 
vulnerability is present in the application.


**Solution:**

The HTTP-Only flag should be set to disable malicious script access to the cookie values 
such as the session ID value.

	