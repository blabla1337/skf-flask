# Are all passwords hashed, salted and stretched 
-------

## Description:

Verify that account passwords are one way hashed with a salt, and there is sufficient work 
factor to defeat brute force and password hash recovery attacks.

## Solution:

Recommended for password usage are PBKDF functions. PBKDF2 uses a pseudorandom function 
and a configurable number of iterations to derive a cryptographic key from a password. 
Because this process is difficult to reverse (similar to a cryptographic hash function)
but can also be configured to be slow to compute, key derivation functions are ideally 
suited for password hashing use cases.

Another alternative would be bcrypt. bcrypt is a password hashing function designed by 
Niels Provos and David Mazières, based on the Blowfish cipher, and presented at USENIX in 
1999. Besides incorporating a salt to protect against rainbow table attacks, bcrypt is an 
adaptive function: over time, the iteration count can be increased to make it slower, 
so it remains resistant to brute-force search attacks even with increasing computation power.
