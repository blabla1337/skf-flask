## Description:

The software does not validate or incorrectly validates the integrity check values or checksums of a message. This may prevent it from detecting if the data has been modified or corrupted in transmission.

Improper validation of checksums before use results in an unnecessary risk that can easily be mitigated. The protocol specification describes the algorithm used for calculating the checksum. It is then a simple matter of implementing the calculation and verifying that the calculated checksum and the received checksum match. Improper verification of the calculated checksum and the received checksum can lead to far greater consequences.

## Mitigation:


PHASE:Implementation:
Ensure that the checksums present in messages are properly checked in accordance with the protocol specification before they are parsed and used.

