## Description:

The software's resource pool is not large enough to handle peak demand, which allows an attacker to prevent others from accessing the resource by using a (relatively) large number of requests for resources.

Frequently the consequence is a flood of connection or sessions.

## Mitigation:


PHASE:Architecture and Design:
Do not perform resource-intensive transactions for unauthenticated users and/or invalid requests.

PHASE:Architecture and Design:
Consider implementing a velocity check mechanism which would detect abusive behavior.

PHASE:Operation:
Consider load balancing as an option to handle heavy loads.

PHASE:Implementation:
Make sure that resource handles are properly closed when no longer needed.

PHASE:Architecture and Design:
Identify the system's resource intensive operations and consider protecting them from abuse (e.g. malicious automated script which runs the resources out).

