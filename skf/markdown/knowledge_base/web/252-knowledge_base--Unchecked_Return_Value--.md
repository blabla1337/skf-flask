## Description:

The software does not check the return value from a method or function, which can prevent it from detecting unexpected states and conditions.

Two common programmer assumptions are this function call can never fail and it doesn't matter if this function call fails. If an attacker can force the function to fail or otherwise return a value that is not expected, then the subsequent program logic could lead to a vulnerability, because the software is not in a state that the programmer assumes. For example, if the program calls a function to drop privileges but does not check the return code to ensure that privileges were successfully dropped, then the program will continue to operate with the higher privileges.

## Mitigation:


PHASE:Implementation:
Check the results of all functions that return a value and verify that the value is expected.:EFFECTIVENESS:High

PHASE:Implementation:
Ensure that you account for all possible return values from the function.

PHASE:Implementation:
When designing a function, make sure you return a value or throw an exception in case of an error.

