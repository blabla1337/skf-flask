## Description:

The software does not drop privileges before passing control of a resource to an actor that does not have those privileges.

In some contexts, a system executing with elevated permissions will hand off a process/file/etc. to another process or user. If the privileges of an entity are not reduced, then elevated privileges are spread throughout a system and possibly to an attacker.

## Mitigation:


PHASE:Architecture and Design:STRATEGY:Separation of Privilege:
Compartmentalize the system to have safe areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design and that the compartmentalization serves to allow for and further reinforce privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide when it is appropriate to use and to drop system privileges.

PHASE:Architecture and Design Operation:
Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software.

PHASE:Architecture and Design:STRATEGY:Separation of Privilege:
Consider following the principle of separation of privilege. Require multiple conditions to be met before permitting access to a system resource.

