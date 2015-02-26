
The logout functionality should revoke the complete session  

-------

**Description:**
When the logout functionality does not revoke the complete session an attacker could impersonate a user even after the session of a user should be terminated increasing the attackers vector of a succesfull hijacking of a users session.


**Solution:**
The logout functionality should revoke the complete session whenever a user wants to terminate his session.

	