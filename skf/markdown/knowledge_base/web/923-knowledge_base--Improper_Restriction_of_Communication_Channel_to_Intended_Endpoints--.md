## Description:

The software establishes a communication channel to (or from) an endpoint for privileged or protected operations, but it does not properly ensure that it is communicating with the correct endpoint.

Attackers might be able to spoof the intended endpoint from a different system or process, thus gaining the same level of access as the intended endpoint. While this issue frequently involves authentication between network-based clients and servers, other types of communication channels and endpoints can have this weakness.

## Mitigation:
