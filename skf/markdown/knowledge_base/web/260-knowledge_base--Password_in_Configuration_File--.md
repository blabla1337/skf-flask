## Description:

The software stores a password in a configuration file that might be accessible to actors who do not know the password.

This can result in compromise of the system for which the password is used. An attacker could gain access to this file and learn the stored password or worse yet, change the password to one of their choosing.

## Mitigation:


PHASE:Architecture and Design:
Avoid storing passwords in easily accessible locations.

PHASE:Architecture and Design:
Consider storing cryptographic hashes of passwords as an alternative to storing in plaintext.

