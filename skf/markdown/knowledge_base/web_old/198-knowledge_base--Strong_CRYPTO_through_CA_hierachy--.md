##Description:

When you have an offline PKI setup you need to have solid strong crypto layers.
An attacker will look for weak chains in the hierarchy and abuse them when found.
This can lead to Man-In-The-Middle (MITM) attacks and impact the 3 security pillars C.I.A (Confidentiality, Integrity and Availability).

## Solution:

Verify that only strong algorithms, ciphers, and protocols are used, through all the certificate hierarchy,
including root and intermediary certificates of your selected certifying authority.
Because this is always in flux we

recommend using the:
SSLlabs free test https://www.ssllabs.com/ssltest/
OWASP OSAFT : https://www.owasp.org/index.php/O-Saft

These TLS hardening recommendations can then be applied on all servers.
