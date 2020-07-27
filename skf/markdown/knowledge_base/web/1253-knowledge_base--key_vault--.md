##Description:

Keys should remain in a protected key vault at all times. 
In particular, ensure that there is a gap between the threat vectors 
that have direct access to the data and the threat vectors that have direct access to the keys. 
This implies that keys should not be stored on the application or web server 
(assuming that application attackers are part of the relevant threat model).

A key vault helps secure, store and tightly control access to tokens, passwords, certificates and,
encryption keys for protecting secrets and other sensitive data.  

Imagine the use of a keyvault in the following scenario's

* Running a docker container and provisioning it with secrets over CLI
* Checking in API keys in your source repositories
* Encrypting sensitive data at rest

Vault provides encryption as a service with centralized key management to simplify encrypting data 
in transit and at rest across clouds and datacenters.

a Vault can be used to encrypt/decrypt data that is stored elsewhere. The primary use of this is to allow applications to encrypt their data while still storing it in the primary data store.

The benefit of this is that developers do not need to worry about how to properly encrypt data. The responsibility of encryption is on Vault and the security team managing it, and developers just encrypt/decrypt data as needed.

##Mitigation:

centrally store, access, and distribute secrets like API keys,
AWS IAM/STS credentials, SQL/NoSQL databases, X.509 certificates, 
SSH credentials, etc by means of a key vault.

When selecting a key vault that is fit for your needs make sure it has Cryptographic Compliance
towards the FIPS standards.


