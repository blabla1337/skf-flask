
Username enumeration
-------

**Description:**
Whenever an application generates error like:

This username already exsists.

An attacker could enumerate these usernames, enlarging his chance for a succefull brute-force attack.

Same goes for "forgot password" functions.

Whenever a user forgot his passoword make him fill in his email adress rather than a username.


**Solution:**
All error messages should be generalized in order to prevent username enumeration.

	