
Include X-XSS-Protection header
-------

**Description:**

This header enables the Cross-site scripting (XSS) filter built into most recent 
web browsers. It is usually enabled by default anyway, 
so the role of this header is to re-enable the filter for this particular website if it 
was disabled by the user. This header is supported in IE 8 and in Chrome 4.


**Solution:**

These headers are also known as the: X-XSS-Protection: 1; mode=block and provide protection 
against XSS attacks when implemented in the application or web-server.

	