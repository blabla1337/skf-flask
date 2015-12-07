
Are all passwords hashed, salted and stretched 
-------

**Description:**

Whenever a password is not properly hashed, salted and stretched an attacker could easily 
abuse the password when obtained.


**Solution:**

A user should always be forced to use a proper password when signing in into the application. 
Preferably a pass-phrase instead of a password. this in order to extend the duration 
of a brute-force attack.

Verify that account passwords are protected using an adaptive key derivation function.
Make sure the salt for the user is always unique and you apply bcrypt, scrypt or 
PBKDF2 before storing the password, with a minimum work factor iteration count of 150,000 
loops to eliminate the possibility of brute forcing. 
	