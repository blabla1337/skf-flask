## Description:

The code transmits data to another actor, but the data contains sensitive information that should not be accessible to the actor that is receiving the data.

Sensitive information could include data that is sensitive in and of itself (such as credentials or private messages), or otherwise useful in the further exploitation of the system (such as internal file system structure).

## Mitigation:


PHASE:Requirements:
Specify which data in the software should be regarded as sensitive. Consider which types of users should have access to which types of data.

PHASE:Implementation:
Ensure that any possibly sensitive data specified in the requirements is verified with designers to ensure that it is either a calculated risk or mitigated elsewhere. Any information that is not necessary to the functionality should be removed in order to lower both the overhead and the possibility of security sensitive data being sent.

PHASE:System Configuration:
Setup default error messages so that unexpected errors do not disclose sensitive information.

PHASE:Architecture and Design:STRATEGY:Separation of Privilege:
Compartmentalize the system to have safe areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design and that the compartmentalization serves to allow for and further reinforce privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide when it is appropriate to use and to drop system privileges.

