## Description:

The software writes to a buffer using an index or pointer that references a memory location prior to the beginning of the buffer.

This typically occurs when a pointer or its index is decremented to a position before the buffer, when pointer arithmetic results in a position before the beginning of the valid memory location, or when a negative index is used.

## Mitigation:


PHASE

DESCRIPTION:Requirements specification: The choice could be made to use a language that is not susceptible to these issues.

PHASE:Implementation:
Sanity checks should be performed on all calculated values used as index or for pointer arithmetic.

