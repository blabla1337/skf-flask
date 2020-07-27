##Description:

The software does not properly restrict reading from or writing to dynamically-managed code resources such as variables, objects, classes, attributes, functions, or executable instructions or statements.

Many languages offer powerful features that allow the programmer to dynamically create or modify existing code, or resources used by code such as variables and objects. While these features can offer significant flexibility and reduce development time, they can be extremely dangerous if attackers can directly influence these code resources in unexpected ways.

##Mitigation:


PHASE:Implementation:STRATEGY:Input Validation:
For any externally-influenced input, check the input against a white list of acceptable values.

PHASE:Implementation Architecture and Design:STRATEGY:Refactoring:
Refactor the code so that it does not need to be dynamically managed.

