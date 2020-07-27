##Description:

The software does not sufficiently track and release allocated memory after it has been used, which slowly consumes remaining memory.

This is often triggered by improper handling of malformed data or unexpectedly interrupted sessions. In some languages, developers are responsible for tracking memory allocation and releasing the memory. If there are no more pointers or references to the memory, then it can no longer be tracked and identified for release.

##Mitigation:


PHASE:Implementation:STRATEGY:Libraries or Frameworks:
Choose a language or tool that provides automatic memory management, or makes manual memory management less error-prone. For example, glibc in Linux provides protection against free of invalid pointers. When using Xcode to target OS X or iOS, enable automatic reference counting (ARC) [REF-391]. To help correctly and consistently manage memory when programming in C++, consider using a smart pointer class such as std

auto_ptr (defined by ISO/IEC ISO/IEC 14882:2003), std

shared_ptr and std

unique_ptr (specified by an upcoming revision of the C++ standard, informally referred to as C++ 1x), or equivalent solutions such as Boost.

PHASE:Architecture and Design:
Use an abstraction library to abstract away risky APIs. Not a complete solution.

PHASE:Architecture and Design Build and Compilation:
The Boehm-Demers-Weiser Garbage Collector or valgrind can be used to detect leaks in code.

