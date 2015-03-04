
Username enumeration
-------

**Description:**

Whenever an application generates error like:

    This username already exsists.

An attacker could enumerate these usernames, enlarging his chance for a succefull brute-force attack. Same goes for &#34;forgot password&#34; functions.

Whenever an user forgot his password then make him fill in his email adress rather than an username.


**Solution:**

All error messages should be generalized in order to prevent username enumeration. Also sometimes you cannot avoid leaking information for example a registration page. Here you need to use tar-pitting methods to prevent an automated attack by an attacker.

	