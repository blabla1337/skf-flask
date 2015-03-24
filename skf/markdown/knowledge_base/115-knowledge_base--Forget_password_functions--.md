
Forget password functions
-------

**Description:**

Whenever a new password is sent by email to the user after using a password forget functionality
this password should never be send to the user directly.


**Solution:**

The forget password function should never send a new password by email but should contain 
a reset link with a token which is valid for a limited amount of time. 
Additional authentication based on soft-tokens 
(e.g. SMS token, native mobile applications, etc.) can be required as well before the 
link is sent over.

	