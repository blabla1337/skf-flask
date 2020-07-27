##Description:

The 'SameSite' cookie attribute helps developers to control if a cookie can be sent along in requests initiated by third-party sites or cross-site requests, helping to prevent Cross-Site-Request-Forgery(CSRF) type of attacks.
The attribute accepts 2 values: strict and lax.
- strict: The cookie will NOT be transmitted within requests initiated by third-party sites, even if initiated by a GET request.
- lax: The cookie will be sent along with GET request only if a Top Level Navigation occurs.


## Solution:

When creating a new cookie in browser, add the 'SameSite' attribute.
