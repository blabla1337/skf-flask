
Access control failure
-------

**Description:**

Handling errors securely is a key aspect of secure coding. There are two types of errors 
that deserve special attention. The first is exceptions that occur in the processing of a 
security control itself. It is important that these exceptions do not enable behaviour 
that the countermeasures would normally not allow. As a developer, you should consider 
that there are generally three possible outcomes from a security 
mechanism: allow the operation, disallow the operation, exception In general. 
You should design your security mechanism so that a failure will follow the same 
execution path as disallowing the operation.


**Solution:**

Security methods like isAuthorized(), isAuthenticated(), and validate() should all return 
false if there is an exception during processing. 
If security controls can throw exceptions, they must be very clear about exactly what that 
condition means. 

	