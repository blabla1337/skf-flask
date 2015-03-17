
The logout functionality should revoke the complete session  
-------

**Description:**

When the logout functionality does not revoke the complete session an attacker could 
impersonate an user when he has access to the session cookie.


**Solution:**

The logout functionality should revoke the complete session whenever a user 
wants to terminate his session.

	