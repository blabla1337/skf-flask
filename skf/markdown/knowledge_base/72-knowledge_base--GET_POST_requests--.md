
GET/POST requests
-------

**Description:**

Authors of services which use the HTTP protocol SHOULD NOT use GET based forms for the 
submission of sensitive data, because this will cause this data to be 
encoded in the Request-URI. Many existing servers, proxies, 
and browsers will log the request URI in some place where it might be 
visible to third parties. Servers can use POST-based form submission instead. 
GET parameters are also more likely to be vulnerable to XSS. Please refer to the 
XSS manual in the knowledge base for more information.


**Solution:**

Whenever transmitting sensitive data always do this by means of the POST request.

	