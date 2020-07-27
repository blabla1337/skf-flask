##Description:

The software does not check or incorrectly checks the revocation status of a certificate, which may cause it to use a certificate that has been compromised.

An improper check for certificate revocation is a far more serious flaw than related certificate failures. This is because the use of any revoked certificate is almost certainly malicious. The most common reason for certificate revocation is compromise of the system in question, with the result that no legitimate servers will be using a revoked certificate, unless they are sorely out of sync.

##Mitigation:


PHASE:Architecture and Design:
Ensure that certificates are checked for revoked status.

PHASE:Implementation:
If certificate pinning is being used, ensure that all relevant properties of the certificate are fully validated before the certificate is pinned, including the revoked status.

