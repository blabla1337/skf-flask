## Description:

Not using a random initialization Vector (IV) with Cipher Block Chaining (CBC) Mode causes algorithms to be susceptible to dictionary attacks.



## Mitigation:


PHASE:Implementation:
It is important to properly initialize CBC operating block ciphers or their utility is lost.

