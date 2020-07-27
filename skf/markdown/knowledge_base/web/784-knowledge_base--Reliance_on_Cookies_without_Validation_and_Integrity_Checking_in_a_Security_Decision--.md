##Description:

The application uses a protection mechanism that relies on the existence or values of a cookie, but it does not properly ensure that the cookie is valid for the associated user.

Attackers can easily modify cookies, within the browser or by implementing the client-side code outside of the browser. Attackers can bypass protection mechanisms such as authorization and authentication by modifying the cookie to contain an expected value.

##Mitigation:


PHASE:Architecture and Design:
Avoid using cookie data for a security-related decision.

PHASE:Implementation:
Perform thorough input validation (i.e.: server side validation) on the cookie data if you're going to use it for a security related decision.

PHASE:Architecture and Design:
Add integrity checks to detect tampering.

PHASE:Architecture and Design:
Protect critical cookies from replay attacks, since cross-site scripting or other attacks may allow attackers to steal a strongly-encrypted cookie that also passes integrity checks. This mitigation applies to cookies that should only be valid during a single transaction or session. By enforcing timeouts, you may limit the scope of an attack. As part of your integrity check, use an unpredictable, server-side value that is not exposed to the client.

