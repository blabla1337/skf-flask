##Description:
Exception handling is the process of responding to the occurrence, during computation, 
of exceptions – anomalous or exceptional conditions requiring special processing 
often disrupting the normal flow of program execution. It is provided by specialized 
programming language constructs, computer hardware mechanisms like interrupts or operating 
system IPC facilities like signals.

In general, an exception breaks the normal flow of execution and executes a pre-registered 
exception handler. The details of how this is done depends on whether it is a hardware or 
software exception and how the software exception is implemented. Some exceptions, 
especially hardware ones, may be handled so gracefully that execution can resume where it was interrupted.

Alternative approaches to exception handling in software are error checking, 
which maintains normal program flow with later explicit checks for contingencies 
reported using special return values or some auxiliary global variable 
such as C's errno or floating point status flags; or input validation to preemptively 
filter exceptional cases.

## Solution:

By catching all different errors and exceptions your program will never be redirected in a 
excecution flow that causes unexpected behaviour. This behaviour could include bypassing authorization 
logic or other sanity checks that could be used to attack the target system.

