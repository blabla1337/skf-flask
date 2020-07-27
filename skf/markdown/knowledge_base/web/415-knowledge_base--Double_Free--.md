##Description:

The product calls free() twice on the same memory address, potentially leading to modification of unexpected memory locations.

When a program calls free() twice with the same argument, the program's memory management data structures become corrupted. This corruption can cause the program to crash or, in some circumstances, cause two later calls to malloc() to return the same pointer. If malloc() returns the same value twice and the program later gives the attacker control over the data that is written into this doubly-allocated memory, the program becomes vulnerable to a buffer overflow attack.

##Mitigation:


PHASE:Architecture and Design:
Choose a language that provides automatic memory management.

PHASE:Implementation:
Ensure that each allocation is freed only once. After freeing a chunk, set the pointer to NULL to ensure the pointer cannot be freed again. In complicated error conditions, be sure that clean-up routines respect the state of allocation properly. If the language is object oriented, ensure that object destructors delete each chunk of memory only once.

PHASE:Implementation:
Use a static analysis tool to find double free instances.

