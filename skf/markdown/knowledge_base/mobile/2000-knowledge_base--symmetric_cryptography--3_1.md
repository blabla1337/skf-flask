## Description:

Symmetric Cryptography

MSTG-CRYPTO-1: The app does not rely on symmetric cryptography with hardcoded keys as a sole method of encryption.

Symmetric-key encryption algorithms use the same key for both encryption and decryption. This type of encryption is fast and suitable for bulk data processing. Since everybody who has access to the key is able to decrypt the encrypted content, this method requires careful key management.

The security of symmetric encryption and keyed hashes (MACs) depends on the secrecy of the key. If the key is disclosed, the security gained by encryption is lost. To prevent this, never store secret keys in the same place as the encrypted data they helped create. A common mistake is encrypting locally stored data with a static, hardcoded encryption key and compiling that key into the app. This makes the key accessible to anyone who can use a disassembler.


## Mitigation:

Encryption key should not be:
	- part of application resources
	- value which can be derived from known values
	- hardcoded in code