
Predictable password and/or token generation
-------

**Description:**

Tokens or passwords that are used within the application must contain a high entropy in 
order to prevent the prediction of these values. 


**Solution:**

Tokens should contain a high level entropy and randomness to prevent predictable token generation.
All random numbers, random file names, random GUIDs, and random must be generated using 
the cryptographic module's approved random number generator 
when these random values are intended to be unguessable by an attacker
	
