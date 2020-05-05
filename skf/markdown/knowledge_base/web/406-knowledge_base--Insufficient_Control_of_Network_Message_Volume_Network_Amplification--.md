## Description:

The software does not sufficiently monitor or control transmitted network traffic volume, so that an actor can cause the software to transmit more traffic than should be allowed for that actor.

In the absence of a policy to restrict asymmetric resource consumption, the application or system cannot distinguish between legitimate transmissions and traffic intended to serve as an amplifying attack on target systems. Systems can often be configured to restrict the amount of traffic sent out on behalf of a client, based on the client's origin or access level. This is usually defined in a resource allocation policy. In the absence of a mechanism to keep track of transmissions, the system or application can be easily abused to transmit asymmetrically greater traffic than the request or client should be permitted to.

## Mitigation:


PHASE:Architecture and Design:STRATEGY:Separation of Privilege:
An application must make network resources available to a client commensurate with the client's access level.

PHASE:Policy:
Define a clear policy for network resource allocation and consumption.

PHASE:Implementation:
An application must, at all times, keep track of network resources and meter their usage appropriately.

