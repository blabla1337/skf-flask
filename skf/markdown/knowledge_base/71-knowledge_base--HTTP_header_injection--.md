
HTTP header injection
-------

**Description:**

HTTP header injection is a general class of web application security vulnerability which 
occurs when Hypertext Transfer Protocol (HTTP) headers are 
dynamically generated based on user input. Header injection in HTTP responses can allow 
for HTTP response splitting (also known as CRLF, Carriage Return Line Feed), 
Session fixation via the Set-Cookie header, cross-site scripting (XSS), 
and malicious redirect attacks via the location header. HTTP header injection is a 
relatively new area for web-based attacks, and has primarily been pioneered 
by Amit Klein in his work on request/response smuggling/splitting. 
Vulnerabilities due to HTTP header injections such as CRLF are no longer 
feasible due to the fact that multiple header requests are not possible.


**Solution:**

When user-input will be used in HTTP headers then the newlines should be escaped in a 
correct manner.

	