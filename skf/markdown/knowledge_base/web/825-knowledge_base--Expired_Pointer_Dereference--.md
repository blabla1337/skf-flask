##Description:

The program dereferences a pointer that contains a location for memory that was previously valid, but is no longer valid.

When a program releases memory, but it maintains a pointer to that memory, then the memory might be re-allocated at a later time. If the original pointer is accessed to read or write data, then this could cause the program to read or modify data that is in use by a different function or process. Depending on how the newly-allocated memory is used, this could lead to a denial of service, information exposure, or code execution.

##Mitigation:


PHASE:Architecture and Design:
Choose a language that provides automatic memory management.

PHASE:Implementation:
When freeing pointers, be sure to set them to NULL once they are freed. However, the utilization of multiple or complex data structures may lower the usefulness of this strategy.

