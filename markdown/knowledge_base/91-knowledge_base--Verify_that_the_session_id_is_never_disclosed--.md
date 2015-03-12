
Verify that the session id is never disclosed
-------

**Description:**

If the session id is disclosed in the URL the users session id can be easily obtained by 
an attacker and could leak through the referer header towards other severs.


**Solution:**

Session id should never be included in places other than the application cookie header.

	