## Description:

Cryptographic keys management

MSTG-ARCH-8: There is an explicit policy for how cryptographic keys (if any) are managed, and the lifecycle of cryptographic keys is enforced. Ideally, follow a key management standard such as NIST SP 800-57.

Key management refers to management of cryptographic keys in a cryptosystem. This includes dealing with the generation, exchange, storage, use, crypto-shredding (destruction) and replacement of keys. It includes cryptographic protocol design, key servers, user procedures, and other relevant protocols.

Successful key management is critical to the security of a cryptosystem. It is the more challenging side of cryptography in a sense that it involves aspects of social engineering such as system policy, user training, organizational and departmental interactions, and coordination between all of these elements, in contrast to pure mathematical practices that can be automated.


## Mitigation:

Cryptographic key management within an application is important to document and harmonize rules and practices for:

	1. Key life cycle management (generation, distribution, destruction)
	2. Key compromise, recovery and zeroization
	3. Key storage
	4. Key agreement
