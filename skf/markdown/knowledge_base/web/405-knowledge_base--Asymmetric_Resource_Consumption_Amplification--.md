## Description:

Software that does not appropriately monitor or control resource consumption can lead to adverse system performance.

This situation is amplified if the software allows malicious users or attackers to consume more resources than their access level permits. Exploiting such a weakness can lead to asymmetric resource consumption, aiding in amplification attacks against the system or the network.

## Mitigation:


PHASE:Architecture and Design:
An application must make resources available to a client commensurate with the client's access level.

PHASE:Architecture and Design:
An application must, at all times, keep track of allocated resources and meter their usage appropriately.

