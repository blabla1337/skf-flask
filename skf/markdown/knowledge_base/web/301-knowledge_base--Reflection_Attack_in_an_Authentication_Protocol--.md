## Description:

Simple authentication protocols are subject to reflection attacks if a malicious user can use the target machine to impersonate a trusted user.

A mutual authentication protocol requires each party to respond to a random challenge by the other party by encrypting it with a pre-shared key. Often, however, such protocols employ the same pre-shared key for communication with a number of different entities. A malicious user or an attacker can easily compromise this protocol without possessing the correct key by employing a reflection attack on the protocol.

## Mitigation:


PHASE:Architecture and Design:
Use different keys for the initiator and responder or of a different type of challenge for the initiator and responder.

PHASE:Architecture and Design:
Let the initiator prove its identity before proceeding.

