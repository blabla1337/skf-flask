
Username enumeration
-------

**Description:**

Whenever an application generates an error like:

"This username already exists"

An attacker could enumerate these usernames, enlarging his chance for a successful 
brute-force attack. Same goes for "Password forget" functions.

Whenever an user forgot his password, make him fill in his email address 
rather than an username.


**Solution:**

All error messages should be generalised in order to prevent username enumeration. 
Also sometimes you cannot avoid information leaking in functionalities such as a 
registration page. Here you need to use tar-pitting methods to prevent an automated 
attack by an attacker.

Also recommended knowledge-base item:

- Differential analysis attack 