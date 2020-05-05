## Description:

The software does not properly restrict reading from or writing to dynamically-identified variables.

Many languages offer powerful features that allow the programmer to access arbitrary variables that are specified by an input string. While these features can offer significant flexibility and reduce development time, they can be extremely dangerous if attackers can modify unintended variables that have security implications.

## Mitigation:


PHASE:Implementation:STRATEGY:Input Validation:
For any externally-influenced input, check the input against a white list of internal program variables that are allowed to be modified.

PHASE:Implementation Architecture and Design:STRATEGY:Refactoring:
Refactor the code so that internal program variables do not need to be dynamically identified.

