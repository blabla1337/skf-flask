## Description:

Storing a password in plaintext may result in a system compromise.

Password management issues occur when a password is stored in plaintext in an application's properties or configuration file. Storing a plaintext password in a configuration file allows anyone who can read the file access to the password-protected resource.

## Mitigation:


PHASE:Architecture and Design:
Avoid storing passwords in easily accessible locations.

PHASE:Architecture and Design:
Consider storing cryptographic hashes of passwords as an alternative to storing in plaintext.

PHASE

DESCRIPTION:A programmer might attempt to remedy the password management problem by obscuring the password with an encoding function, such as base 64 encoding, but this effort does not adequately protect the password because the encoding can be detected and decoded easily.:EFFECTIVENESS:None

