## Description:

The software uses a cookie to store sensitive information, but the cookie is not marked with the HttpOnly flag.

The HttpOnly flag directs compatible browsers to prevent client-side script from accessing cookies. Including the HttpOnly flag in the Set-Cookie HTTP response header helps mitigate the risk associated with Cross-Site Scripting (XSS) where an attacker's script code might attempt to read the contents of a cookie and exfiltrate information obtained. When set, browsers that support the flag will not reveal the contents of the cookie to a third party via client-side script executed via XSS.

## Mitigation:


PHASE:Implementation:
Leverage the HttpOnly flag when setting a sensitive cookie in a response.:EFFECTIVENESS:High

