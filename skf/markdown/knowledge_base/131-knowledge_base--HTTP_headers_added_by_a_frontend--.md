
HTTP headers added by a front-end
-------

**Description:**

Use these kind of HTTP headers (X-Forwarded-For) only if you have a front-end proxy.


**Solution:**

As with the X-Forwarded-For option above, only use this option if you want to retrieve 
the visitor IP address from the X-Forwarded-For HTTP header and do not enable this if you 
don't have a front-end proxy or load balancer that is sending visits to your real 
web-server and adding the X-Real-IP header.

	