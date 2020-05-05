## Description:

The software does not properly assign, modify, track, or check privileges for an actor, creating an unintended sphere of control for that actor.



## Mitigation:


PHASE:Architecture and Design Operation:
Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software.

PHASE:Architecture and Design:STRATEGY:Separation of Privilege:
Follow the principle of least privilege when assigning access rights to entities in a software system.

PHASE:Architecture and Design:STRATEGY:Separation of Privilege:
Consider following the principle of separation of privilege. Require multiple conditions to be met before permitting access to a system resource.

