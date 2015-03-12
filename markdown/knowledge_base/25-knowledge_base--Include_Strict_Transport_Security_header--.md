
Include Strict-Transport-Security header
-------

**Description:**

HTTP Strict-Transport-Security (HSTS) enforces secure (HTTP over SSL/TLS) connections to 
the server. This reduces impact of bugs in web applications leaking session data through 
cookies and external links and defends against Man-in-the-middle attacks. HSTS also 
disables the ability for user's to ignore SSL negotiation warnings


**Solution:**

These headers are also known as the: Strict-Transport-Security: max-age=16070400: 
includeSubDomains and provide protection against SSL Strip attacks when implemented in the
application or webserver. 

	