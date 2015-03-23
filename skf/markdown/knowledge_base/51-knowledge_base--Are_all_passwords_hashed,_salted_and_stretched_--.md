
Are all passwords hashed, salted and stretched 
-------

**Description:**

Whenever a password is not properly hashed, salted and stretched an attacker could easily 
abuse the password when obtained.


**Solution:**

A user should always be forced to use a proper password when signing in into the application. 
Preferably a pass-phrase instead of a password. this in order to extend the duration 
of a brute-force attack.

Also before storing this password into the database the passwords should be salted and 
hashed properly only using proven cryptographic algorithms like sha256 or AES.

	