## Description:

The program omits a break statement within a switch or similar construct, causing code associated with multiple conditions to execute. This can cause problems when the programmer only intended to execute code associated with one condition.

This can lead to critical code executing in situations where it should not.

## Mitigation:


PHASE:Implementation:
Omitting a break statement so that one may fall through is often indistinguishable from an error, and therefore should be avoided. If you need to use fall-through capabilities, make sure that you have clearly documented this within the switch statement, and ensure that you have examined all the logical possibilities.

PHASE:Implementation:
The functionality of omitting a break statement could be clarified with an if statement. This method is much safer.

