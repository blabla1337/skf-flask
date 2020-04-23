## Description:

The software communicates with a host that provides a certificate, but the software does not properly ensure that the certificate is actually associated with that host.

Even if a certificate is well-formed, signed, and follows the chain of trust, it may simply be a valid certificate for a different site than the site that the software is interacting with. If the certificate's host-specific data is not properly checked - such as the Common Name (CN) in the Subject or the Subject Alternative Name (SAN) extension of an X.509 certificate - it may be possible for a redirection or spoofing attack to allow a malicious host with a valid certificate to provide data, impersonating a trusted host. In order to ensure data integrity, the certificate must be valid and it must pertain to the site that is being accessed. Even if the software attempts to check the hostname, it is still possible to incorrectly check the hostname. For example, attackers could create a certificate with a name that begins with a trusted name followed by a NUL byte, which could cause some string-based comparisons to only examine the portion that contains the trusted name. This weakness can occur even when the software uses Certificate Pinning, if the software does not verify the hostname at the time a certificate is pinned.

## Mitigation:


PHASE:Architecture and Design:
Fully check the hostname of the certificate and provide the user with adequate information about the nature of the problem and how to proceed.

PHASE:Implementation:
If certificate pinning is being used, ensure that all relevant properties of the certificate are fully validated before the certificate is pinned, including the hostname.

