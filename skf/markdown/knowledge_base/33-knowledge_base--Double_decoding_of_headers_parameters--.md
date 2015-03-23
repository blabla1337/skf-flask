
Double decoding of headers/parameters
-------

**Description:**

Double decoding is a problem which often occurs when multiple servers are used in which a 
configuration error is made. 
A hacker can encode his payload differently so it will not be recognised by an WAF or IDS 
and also bypass the escaping of the application.


**Solution:**

Only one web-server should decode/encode the data.
	