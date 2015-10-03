
Automatic variable binding
-------

**Description:**

If the application framework allows automatic mass parameter assignment 
(also called automatic variable binding) from the inbound request to a model, 
verify that security sensitive fields such as 'accountBalance', 'role' or 'password' 
are protected from malicious automatic binding. Whenever your application takes parameters 
in HTTPs GET statement and passes them as variables to code within the application this 
could become a safety hazard since the application processes these variables 
in his operations.


**Solution:**

When working with automatic variable binding you should create whitelists of what 
parameters are expected and allow only these parameters to be passed into your 
application operation.
