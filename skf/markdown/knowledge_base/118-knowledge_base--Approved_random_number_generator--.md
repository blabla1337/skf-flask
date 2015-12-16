
Approved random number generator
-------

**Description:**

The lack of entropy available for, or used by, a pseudo-random number generator can be a 
stability and security threat.


**Solution:**

All random numbers, random file names, random GUIDs, and random must be generated using 
the cryptographic module's approved random number generator when these random values are 
intended to be unguessable/unpredictable by an attacker.
	