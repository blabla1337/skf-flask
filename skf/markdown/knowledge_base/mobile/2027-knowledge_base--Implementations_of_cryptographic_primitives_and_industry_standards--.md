## Description:

Implementations of cryptographic primitives and industry standards

MSTG-CRYPTO-2: The app uses proven implementations of cryptographic primitives.

MSTG-CRYPTO-3: The app uses cryptographic primitives that are appropriate for the particular use-case, configured with parameters that adhere to industry best practices.


## Mitigation:

To focus on implementation and use of cryptographic primitives, following checks should be performed:

	- identify all instance of cryptography primitives and their implementation (library or custom implementation)
	- verify how cryptography primitives are used and how they are configured
	- verify if cryptographic protocols and algorithms used are not deprecated for security purposes.
