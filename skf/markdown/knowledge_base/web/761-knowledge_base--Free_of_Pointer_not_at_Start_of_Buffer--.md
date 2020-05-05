## Description:

The application calls free() on a pointer to a memory resource that was allocated on the heap, but the pointer is not at the start of the buffer.

This can cause the application to crash, or in some cases, modify critical program variables or execute code. This weakness often occurs when the memory is allocated explicitly on the heap with one of the malloc() family functions and free() is called, but pointer arithmetic has caused the pointer to be in the interior or end of the buffer.

## Mitigation:


PHASE:Implementation:
When utilizing pointer arithmetic to traverse a buffer, use a separate variable to track progress through memory and preserve the originally allocated address for later freeing.

PHASE:Implementation:
When programming in C++, consider using smart pointers provided by the boost library to help correctly and consistently manage memory.

PHASE:Architecture and Design:STRATEGY:Libraries or Frameworks:
Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, glibc in Linux provides protection against free of invalid pointers.

PHASE:Architecture and Design:
Use a language that provides abstractions for memory allocation and deallocation.

PHASE:Testing:
Use a tool that dynamically detects memory management problems, such as valgrind.

