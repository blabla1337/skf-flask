## Description:

Payload encryption

MSTG-RESILIENCE-13: As a defense in depth, next to having solid hardening of the communicating parties, application level payload encryption can be applied to further impede eavesdropping.

Payload Encryption provides an additional layer security and it is not an alternative for TLS protocols.

The application should encrypt and sign payloads (for example HTTP parameters) before sending them to back-end services. It is a defense in depth approach, and even HTTPS requests somehow are intercepted, the communication will be still confidential.


## Mitigation:

A proper encrypted payload should provide confidentiality, integrity and additionally it should be non-repudiation. Therefore, key and certificate management might be required.
