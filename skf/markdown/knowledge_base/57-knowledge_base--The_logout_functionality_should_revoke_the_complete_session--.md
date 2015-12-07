
The logout functionality should revoke the complete session  
-------

**Description:**

When the logout functionality does not revoke the complete session an attacker could 
impersonate a user when he has access to the session cookie.


**Solution:**

The logout functionality should revoke the complete session whenever a user 
wants to terminate his session. 

Each different framework has its own guide to achieve this revocation.
It is also recommended for you to make testcases which you follow to ensure 
session revocation in your application.




