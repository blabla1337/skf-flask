##Description:

A certificate expiration is not validated or is incorrectly validated, so trust may be assigned to certificates that have been abandoned due to age.

When the expiration of a certificate is not taken into account, no trust has necessarily been conveyed through it. Therefore, the validity of the certificate cannot be verified and all benefit of the certificate is lost.

##Mitigation:


PHASE:Architecture and Design:
Check for expired certificates and provide the user with adequate information about the nature of the problem and how to proceed.

PHASE:Implementation:
If certificate pinning is being used, ensure that all relevant properties of the certificate are fully validated before the certificate is pinned, including the expiration.

