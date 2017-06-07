# Session cookies without the HttpOnly flag
-------

## Description:

An HttpOnly flag is an option that can be set when creating a cookie. This flag ensures that the cookie cannot be read or edited by JavaScript. This ensures an attacker cannot steal this cookie as a cross-site scripting vulnerability is present in the application.

## Solution:

The HttpOnly flag should be set to disable malicious script access to the cookie values such as the session ID value. Also, disable unnecessary HTTP request methods because of the TRACE option. Misconfiguration of the HTTP request headers can lead to stealing the session cookie even though HttpOnly protection is in place.

Recommended knowledge base items:

- HTTP request methods
- Session management
