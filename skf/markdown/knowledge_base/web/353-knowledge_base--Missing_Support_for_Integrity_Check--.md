##Description:

The software uses a transmission protocol that does not include a mechanism for verifying the integrity of the data during transmission, such as a checksum.

If integrity check values or checksums are omitted from a protocol, there is no way of determining if data has been corrupted in transmission. The lack of checksum functionality in a protocol removes the first application-level check of data that can be used. The end-to-end philosophy of checks states that integrity checks should be performed at the lowest level that they can be completely implemented. Excluding further sanity checks and input validation performed by applications, the protocol's checksum is the most important level of checksum, since it can be performed more completely than at any previous level and takes into account entire messages, as opposed to single packets.

##Mitigation:


PHASE:Architecture and Design:
Add an appropriately sized checksum to the protocol, ensuring that data received may be simply validated before it is parsed and used.

PHASE:Implementation:
Ensure that the checksums present in the protocol design are properly implemented and added to each message before it is sent.

