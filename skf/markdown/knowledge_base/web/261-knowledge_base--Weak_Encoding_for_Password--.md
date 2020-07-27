##Description:

Obscuring a password with a trivial encoding does not protect the password.

Password management issues occur when a password is stored in plaintext in an application's properties or configuration file. A programmer can attempt to remedy the password management problem by obscuring the password with an encoding function, such as base 64 encoding, but this effort does not adequately protect the password.

##Mitigation:


PHASE

DESCRIPTION:Passwords should be encrypted with keys that are at least 128 bits in length for adequate security.

