## Description:

The software establishes a communication channel to handle an incoming request that has been initiated by an actor, but it does not properly verify that the request is coming from the expected origin.

When an attacker can successfully establish a communication channel from an untrusted origin, the attacker may be able to gain privileges and access unexpected functionality.

## Mitigation:


PHASE:Architecture and Design:
Use a mechanism that can validate the identity of the source, such as a certificate, and validate the integrity of data to ensure that it cannot be modified in transit using a MITM attack. When designing functionality of actions in the URL scheme, consider whether the action should be accessible to all mobile applications, or if a whitelist of applications to interface with is appropriate.

