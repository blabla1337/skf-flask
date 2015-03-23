
cryptographic modules must fail securely
-------

**Description:**

Whenever a cryptographic module does not fail securely this the device needs to be put in 
error state so it's not useable anymore.


**Solution:**

We recommend using the NIST standard on testing the cryptographic module making it perform 
the self-tests to see if it fails securely.

	