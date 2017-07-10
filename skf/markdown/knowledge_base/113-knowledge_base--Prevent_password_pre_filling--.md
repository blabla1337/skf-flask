## Description:

Passwords should never be stored plaintext or in a reversible format on the application. Whenever an attacker hacks 
into the applications SQL database the passwords are directly compromised. In the case of
pre-filled forms in the application, an attacker could also hijack the credentials by badly
configured CORS rules or XSS attacks.

## Solution: 

Verify that forms containing credentials are not filled in by
the application. Pre-filling by the application implies that
credentials are stored in plaintext or a reversible format,
which is explicitly prohibited. Passwords should be stored by preferably PBKDF functions.

PBKDF2 uses a pseudorandom function and a configurable number of iterations to derive a
cryptographic key from a password. Because this process is difficult to reverse
(similar to a cryptographic hash function) but can also be configured to be slow to 
compute, key derivation functions are ideally suited for password hashing use cases.

Examples of good ways to store passwords are with, BCRYPT, Blowfish or in some cases SCRYPT
which is a little harder to implement correctly

NOTE: Password pre-filling also happens when using the browsers password manager. For the login input
fields the 'autocomplete=off' HTML attribute should be added to disable the password manager. The credentials
could otherwise be stolen by XSS attacks whenever an attacker injects an HTML login form into the application
which is pre-filled by the password manager.
