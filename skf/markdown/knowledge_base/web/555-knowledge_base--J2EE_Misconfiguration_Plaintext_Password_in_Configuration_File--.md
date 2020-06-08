## Description:

The J2EE application stores a plaintext password in a configuration file.

Storing a plaintext password in a configuration file allows anyone who can read the file to access the password-protected resource, making it an easy target for attackers.

## Mitigation:


PHASE:Architecture and Design:
Do not hardwire passwords into your software.

PHASE:Architecture and Design:
Use industry standard libraries to encrypt passwords before storage in configuration files.

