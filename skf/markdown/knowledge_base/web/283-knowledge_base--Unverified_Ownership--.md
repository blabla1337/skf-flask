##Description:

The software does not properly verify that a critical resource is owned by the proper entity.



##Mitigation:


PHASE:Architecture and Design Operation:
Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software.

PHASE:Architecture and Design:STRATEGY:Separation of Privilege:
Consider following the principle of separation of privilege. Require multiple conditions to be met before permitting access to a system resource.

