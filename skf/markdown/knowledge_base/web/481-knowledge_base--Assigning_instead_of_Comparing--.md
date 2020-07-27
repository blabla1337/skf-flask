##Description:

The code uses an operator for assignment when the intention was to perform a comparison.

In many languages the compare statement is very close in appearance to the assignment statement and are often confused. This bug is generally the result of a typo and usually causes obvious problems with program execution. If the comparison is in an if statement, the if statement will usually evaluate the value of the right-hand side of the predicate.

##Mitigation:


PHASE:Testing:
Many IDEs and static analysis products will detect this problem.

PHASE:Implementation:
Place constants on the left. If one attempts to assign a constant with a variable, the compiler will of course produce an error.

