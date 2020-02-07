## Description:

Whenever an application provides TLS, all connections should be TLS otherwise the
encryption will be lost.

## Solution:

Verify that TLS is used for all connections
(including both external and backend connections) that are using authentication tokens or
that involve sensitive data or functions.
This should also be enforced in the application itself wherever possible,
for example: Secure flags on cookies, HSTS, certificate pinning etc.
