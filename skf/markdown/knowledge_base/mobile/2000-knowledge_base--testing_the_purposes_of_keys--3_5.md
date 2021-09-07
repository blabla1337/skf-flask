## Description:

Testing the Purposes of Keys

MSTG-CRYPTO-5: The app doesn’t re-use the same cryptographic key for multiple purposes.

A different encryption key should be used for different tasks.


## Mitigation:

To focus on verification of purpose and reusage of the same cryptographic keys, following checks should be performed:

	* identify all instances where cryptography is used
	* identify purpose why cryptography is used (to protect data in use, in transit or at rest)
	* identify type of cryptography 
	* verify if cryptography is used according to its purpose
