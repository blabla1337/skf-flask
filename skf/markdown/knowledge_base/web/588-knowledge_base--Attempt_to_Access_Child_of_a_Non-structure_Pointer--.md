## Description:

Casting a non-structure type to a structure type and accessing a field can lead to memory access errors or data corruption.



## Mitigation:


PHASE:Requirements:
The choice could be made to use a language that is not susceptible to these issues.

PHASE:Implementation:
Review of type casting operations can identify locations where incompatible types are cast.

