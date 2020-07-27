##Description:

In C and C++, one may often accidentally refer to the wrong memory due to the semantics of when math operations are implicitly scaled.



##Mitigation:


PHASE:Architecture and Design:
Use a platform with high-level memory abstractions.

PHASE:Implementation:
Always use array indexing instead of direct pointer manipulation.

PHASE:Architecture and Design:
Use technologies for preventing buffer overflows.

