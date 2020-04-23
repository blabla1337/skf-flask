## Description:

The product, upon installation, sets incorrect permissions for an object that exposes it to an unintended actor.



## Mitigation:


PHASE:Architecture and Design Operation:
Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software.

PHASE:Architecture and Design:STRATEGY:Separation of Privilege:
Compartmentalize the system to have safe areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design and that the compartmentalization serves to allow for and further reinforce privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide when it is appropriate to use and to drop system privileges.

