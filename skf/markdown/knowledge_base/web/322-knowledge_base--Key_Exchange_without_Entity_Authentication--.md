## Description:

The software performs a key exchange with an actor without verifying the identity of that actor.

Performing a key exchange will preserve the integrity of the information sent between two entities, but this will not guarantee that the entities are who they claim they are. This may enable an attacker to impersonate an actor by modifying traffic between the two entities. Typically, this involves a victim client that contacts a malicious server that is impersonating a trusted server. If the client skips authentication or ignores an authentication failure, the malicious server may request authentication information from the user. The malicious server can then use this authentication information to log in to the trusted server using the victim's credentials, sniff traffic between the victim and trusted server, etc.

## Mitigation:


PHASE:Architecture and Design:
Ensure that proper authentication is included in the system design.

PHASE:Implementation:
Understand and properly implement all checks necessary to ensure the identity of entities involved in encrypted communications.

