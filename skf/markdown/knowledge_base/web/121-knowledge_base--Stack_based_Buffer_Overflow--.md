##Description:

A stack-based buffer overflow condition is a condition where the buffer being overwritten is allocated on the stack (i.e., is a local variable or, rarely, a parameter to a function).



##Mitigation:


PHASE:Build and Compilation:STRATEGY:Compilation or Build Hardening:
Run or compile the software using features or extensions that automatically provide a protection mechanism that mitigates or eliminates buffer overflows. For example, certain compilers and extensions provide automatic buffer overflow detection mechanisms that are built into the compiled code. Examples include the Microsoft Visual Studio /GS flag, Fedora/Red Hat FORTIFY_SOURCE GCC flag, StackGuard, and ProPolice.:EFFECTIVENESS:Defense in Depth

PHASE:Architecture and Design:
Use an abstraction library to abstract away risky APIs. Not a complete solution.

PHASE:Build and Compilation:
Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.

PHASE:Implementation:
Implement and perform bounds checking on input.

PHASE:Implementation:
Do not use dangerous functions such as gets. Use safer, equivalent functions which check for boundary errors.

PHASE:Operation:
Use OS-level preventative functionality, such as ASLR. This is not a complete solution.

