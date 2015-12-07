
Forget password functions
-------

**Description:**

Whenever a user forgets his password and your application provides a password
forget functionality or any other type of recovery paths
there are a couple of things to take into consideration when you want to harden its 
security.


**Solution:**

The forget password function should never send a new password by email but should contain 
a reset link with a token which is valid for a limited amount of time. 
Additional authentication based on soft-tokens 
(e.g. SMS token, native mobile applications, etc.) can be required as well before the 
link is sent over. Also make sure whenever such a recovery cycle is started, the 
application does not reveal the users current password in any way.

Recommended knowledge-base items:

- Prevent password leaking
- Disallow the use of old passwords
- Predictable password and/or token generation

