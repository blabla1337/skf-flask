
Canonicalized user input
-------

**Description:**

Whenever userinput is partially validated there is a high probability that the application 
misses a malicious input which could execute into a succesfull attack on your application.


**Solution:**

All userinput should be validated whenever the userinput string is complete and is being 
processed by your application.
