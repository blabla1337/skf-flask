## Description:

There should be extra care taken into account when you are dealing with PII(personal identifiable information) in your
application. There are multiple laws in countries that demand proper protection by
means of SSL/TLS for when the data is in transit and encrypted with pub priv key system
when stored on the disk. This is needed to protect the user from identity theft and fraud.

## Solution:

Personally Identifiable Information needs to be stored encrypted at rest ideally in a secured environment such as your vault.
In addition to being able to store secrets, a Vault can be used to encrypt/decrypt data that is stored elsewhere. The primary use of this is to allow applications to encrypt their data while still storing it in the primary data store.

The benefit of this is that developers do not need to worry about how to properly encrypt data. The responsibility of encryption is on Vault and the security team managing it, and developers just encrypt/decrypt data as needed.

Also, ensure that all communication goes via protected channels like SSL/TLS. 
