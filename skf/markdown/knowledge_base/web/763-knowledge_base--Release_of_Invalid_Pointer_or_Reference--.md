## Description:

The application attempts to return a memory resource to the system, but calls the wrong release function or calls the appropriate release function incorrectly.

This weakness can take several forms, such as: The memory was allocated, explicitly or implicitly, via one memory management method and deallocated using a different, non-compatible function (CWE-762). The function calls or memory management routines chosen are appropriate, however they are used incorrectly, such as in CWE-761.

## Mitigation:


PHASE:Implementation:
Only call matching memory management functions. Do not mix and match routines. For example, when you allocate a buffer with malloc(), dispose of the original pointer with free().

PHASE:Implementation:
When programming in C++, consider using smart pointers provided by the boost library to help correctly and consistently manage memory.

PHASE:Architecture and Design:STRATEGY:Libraries or Frameworks:
Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, glibc in Linux provides protection against free of invalid pointers.

PHASE:Architecture and Design:
Use a language that provides abstractions for memory allocation and deallocation.

PHASE:Testing:
Use a tool that dynamically detects memory management problems, such as valgrind.

