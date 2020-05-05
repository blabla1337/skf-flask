## Description:

The accidental deletion of a data-structure sentinel can cause serious programming logic problems.

Often times data-structure sentinels are used to mark structure of the data structure. A common example of this is the null character at the end of strings. Another common example is linked lists which may contain a sentinel to mark the end of the list. It is dangerous to allow this type of control data to be easily accessible. Therefore, it is important to protect from the deletion or modification outside of some wrapper interface which provides safety.

## Mitigation:


PHASE:Architecture and Design:
Use an abstraction library to abstract away risky APIs. Not a complete solution.

PHASE:Build and Compilation:STRATEGY:Compilation or Build Hardening:
Run or compile the software using features or extensions that automatically provide a protection mechanism that mitigates or eliminates buffer overflows. For example, certain compilers and extensions provide automatic buffer overflow detection mechanisms that are built into the compiled code. Examples include the Microsoft Visual Studio /GS flag, Fedora/Red Hat FORTIFY_SOURCE GCC flag, StackGuard, and ProPolice.:EFFECTIVENESS:Defense in Depth

PHASE:Operation:
Use OS-level preventative functionality. Not a complete solution.

