##Description:

An HttpOnly flag is an option that can be set when creating a cookie. This v ensures that the cookie cannot be read or edited by JavaScript. This ensures an attacker cannot steal this cookie as a cross-site scripting vulnerability is present in the application.

##Mitigation:

The HttpOnly flag should be set to disable malicious script access to the cookie values such as the session ID value. Also, disable unnecessary HTTP request methods such as the TRACE option. Misconfiguration of the HTTP request headers can lead to stealing the session cookie even though HttpOnly protection is in place.
