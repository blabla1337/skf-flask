##Description:

The software implements an IOCTL with functionality that should be restricted, but it does not properly enforce access control for the IOCTL.

When an IOCTL contains privileged functionality and is exposed unnecessarily, attackers may be able to access this functionality by invoking the IOCTL. Even if the functionality is benign, if the programmer has assumed that the IOCTL would only be accessed by a trusted process, there may be little or no validation of the incoming data, exposing weaknesses that would never be reachable if the attacker cannot call the IOCTL directly. The implementations of IOCTLs will differ between operating system types and versions, so the methods of attack and prevention may vary widely.

##Mitigation:


PHASE:Architecture and Design:
In Windows environments, use proper access control for the associated device or device namespace. See References.

