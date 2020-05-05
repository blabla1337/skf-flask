## Description:

The software does not validate, or incorrectly validates, a certificate.

When a certificate is invalid or malicious, it might allow an attacker to spoof a trusted entity by interfering in the communication path between the host and client. The software might connect to a malicious host while believing it is a trusted host, or the software might be deceived into accepting spoofed data that appears to originate from a trusted host.

## Mitigation:


PHASE:Architecture and Design Implementation:
Certificates should be carefully managed and checked to assure that data are encrypted with the intended owner's public key.

PHASE:Implementation:
If certificate pinning is being used, ensure that all relevant properties of the certificate are fully validated before the certificate is pinned, including the hostname.

