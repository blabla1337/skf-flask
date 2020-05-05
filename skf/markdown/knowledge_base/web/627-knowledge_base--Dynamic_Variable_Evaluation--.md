## Description:

In a language where the user can influence the name of a variable at runtime, if the variable names are not controlled, an attacker can read or write to arbitrary variables, or access arbitrary functions.

The resultant vulnerabilities depend on the behavior of the application, both at the crossover point and in any control/data flow that is reachable by the related variables or functions.

## Mitigation:


PHASE:Implementation:STRATEGY:Refactoring:
Refactor the code to avoid dynamic variable evaluation whenever possible.

PHASE:Implementation:STRATEGY:Input Validation:
Use only whitelists of acceptable variable or function names.

PHASE:Implementation:
For function names, ensure that you are only calling functions that accept the proper number of arguments, to avoid unexpected null arguments.

