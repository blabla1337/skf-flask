Session cookies without the HttpOnly flag
-------

**Description:**

The http-only flag is an option that can be set when creating a cookie.
This flag ensures that the cookie can not be read or edited by javascript.
This ensures that an attacker can not steal this cookie as a cross-site scripting
vulnerability is present in the application.


**Solution:**

The HTTP-Only flag should be set to disable malicious script access to the cookie values
such as the session ID value. Also disable unnecessary http request methods because of
the TRACE option. Misconfiguration of the HTTP request headers can lead to stealing the
session cookie even though http-only protection is in place.

Recommended knowledge base items:

- HTTP request methods
- Session management
