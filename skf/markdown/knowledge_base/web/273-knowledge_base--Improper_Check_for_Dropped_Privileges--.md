## Description:

The software attempts to drop privileges but does not check or incorrectly checks to see if the drop succeeded.

If the drop fails, the software will continue to run with the raised privileges, which might provide additional access to unprivileged users.

## Mitigation:


PHASE:Architecture and Design:STRATEGY:Separation of Privilege:
Compartmentalize the system to have safe areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design and that the compartmentalization serves to allow for and further reinforce privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide when it is appropriate to use and to drop system privileges.

PHASE:Implementation:
Check the results of all functions that return a value and verify that the value is expected.:EFFECTIVENESS:High

PHASE:Implementation:
In Windows, make sure that the process token has the SeImpersonatePrivilege(Microsoft Server 2003). Code that relies on impersonation for security must ensure that the impersonation succeeded, i.e., that a proper privilege demotion happened.

