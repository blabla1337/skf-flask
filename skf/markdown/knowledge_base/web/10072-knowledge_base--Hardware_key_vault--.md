##Description:

Keys should remain in a protected key vault at all times. In particular, ensure that there
is a gap between the threat vectors that have direct access to the data and the threat
vectors that have direct access to the keys. This implies that keys should not be stored
on the application or web server (assuming that application attackers are part of the
relevant threat model).

##Mitigation:

Verify that all consumers of cryptographic services do not have direct access to key material.
Isolate cryptographic processes, including master secrets and consider the use of a hardware key vault (HSM).
