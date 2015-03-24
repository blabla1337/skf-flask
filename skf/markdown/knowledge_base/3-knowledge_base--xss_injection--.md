
XSS injection
-------

**Description:**

Every time the application gets user-input, whether this showing it on screen or processing
this data in the application background, these paramaters should be escaped for malicious
code in order to prevent cross site scripting injections. 
When an attacker gains the possibility to perform a XSS injection,
he is given the opportunity to inject HTML and javascript code directly into the
application. This could lead to accounts being compromised by stealing session cookies,
or directly affect the operation of the target application.


**Solution:**

In order to prevent XSS injections all user-input should be escaped.
You could start by encoding user-input as soon as it is inserted into the application, 
by preference using a so called white-listing method
This means u should not checking for malicious content like the tags or anything, 
but only allowing the expected input.

The second step would be encoding al the parameters or user-input before putting this in 
your html with encoding libraries specially designed for this purpose. 

Also whenever a user is allowed to add hrefs,  make sure the application checks whether 
the href contains http:// or https://. This is done in order to prevent 
javascript: or data: type XSS injections. 

	