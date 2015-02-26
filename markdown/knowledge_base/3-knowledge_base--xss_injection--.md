
XSS injection
-------

**Description:**
Everytime the application gets userinput, whether this showing it on screen or processing this data in the application
background, these paramaters should be escaped for malicious code in order to prevent cross site scripting injections.
When a attacker gains the possibility to perform a XSS injection, he is given the opportunity to inject HTML and javascript
code directly into the application. This could lead to accounts being compromised by stealing session cookies, or directly affect
the operation of the target application.



**Solution:**
In order to prevent XSS injections all userinput should be escaped. You could start by stripping userinput as soon as it is
inserted into the application, by preference using a so called "white-listing method". This means u should not checking for
malicious content like the tags or anything, but only allowing the expected input. for instacne: when a user is
expected to enter a username, you couldset a regular expression checking only for alphanumerical characters.

Also whenever a user is allowed to add href's, make sure the application checks whether the href contains http:// or https://. This is done in order to prevent javscript: or data: type xss injections. 

	