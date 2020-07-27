##Description:

A function returns the address of a stack variable, which will cause unintended program behavior, typically in the form of a crash.

Because local variables are allocated on the stack, when a program returns a pointer to a local variable, it is returning a stack address. A subsequent function call is likely to re-use this same stack address, thereby overwriting the value of the pointer, which no longer corresponds to the same variable since a function's stack frame is invalidated when it returns. At best this will cause the value of the pointer to change unexpectedly. In many cases it causes the program to crash the next time the pointer is dereferenced.

##Mitigation:


PHASE:Testing:
Use static analysis tools to spot return of the address of a stack variable.

