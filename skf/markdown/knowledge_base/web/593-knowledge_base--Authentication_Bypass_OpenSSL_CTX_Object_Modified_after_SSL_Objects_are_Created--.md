## Description:

The software modifies the SSL context after connection creation has begun.

If the program modifies the SSL_CTX object after creating SSL objects from it, there is the possibility that older SSL objects created from the original context could all be affected by that change.

## Mitigation:


PHASE:Architecture and Design:
Use a language or a library that provides a cryptography framework at a higher level of abstraction.

PHASE:Implementation:
Most SSL_CTX functions have SSL counterparts that act on SSL-type objects.

PHASE:Implementation:
Applications should set up an SSL_CTX completely, before creating SSL objects from it.

