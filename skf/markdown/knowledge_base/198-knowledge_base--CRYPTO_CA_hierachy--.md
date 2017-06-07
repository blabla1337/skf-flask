# Strong Crypto through all the certificate hierarchy
-------

## Description:

When you have an offline PKI setup you need to have solid strong crypto layers.
An attacker will look for weak chains in the hierarchy and abuse them when found.
This can lead to MiTM attacks and impact the 3 security pillars C.I.A.

## Solution:

Verify that only strong algorithms, ciphers, and protocols are used, through all the certificate hierarchy,
including root and intermediary certificates of your selected certifying authority.
Because this is always in flux we recommend using the SSLlabs free test:

https://www.ssllabs.com/ssltest/
These TLS hardening recommendations can then be applied on all servers.
