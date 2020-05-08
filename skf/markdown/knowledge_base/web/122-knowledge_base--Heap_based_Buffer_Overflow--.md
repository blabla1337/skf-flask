## Description:

A heap overflow condition is a buffer overflow, where the buffer that can be overwritten is allocated in the heap portion of memory, generally meaning that the buffer was allocated using a routine such as malloc().



## Mitigation:


PHASE

DESCRIPTION:Pre-design: Use a language or compiler that performs automatic bounds checking.

PHASE:Architecture and Design:
Use an abstraction library to abstract away risky APIs. Not a complete solution.

PHASE:Build and Compilation:
Pre-design through Build: Canary style bounds checking, library changes which ensure the validity of chunk data, and other such fixes are possible, but should not be relied upon.

PHASE:Implementation:
Implement and perform bounds checking on input.

PHASE:Implementation:STRATEGY:Libraries or Frameworks:
Do not use dangerous functions such as gets. Look for their safe equivalent, which checks for the boundary.

PHASE:Operation:
Use OS-level preventative functionality. This is not a complete solution, but it provides some defense in depth.

