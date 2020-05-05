## Description:

True random number generators (TRNG) generally have a limited source of entropy and therefore can fail or block.

The rate at which true random numbers can be generated is limited. It is important that one uses them only when they are needed for security.

## Mitigation:


PHASE:Implementation:
Rather than failing on a lack of random numbers, it is often preferable to wait for more numbers to be created.

