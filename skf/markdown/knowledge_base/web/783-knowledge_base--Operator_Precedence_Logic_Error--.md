##Description:

The program uses an expression in which operator precedence causes incorrect logic to be used.

While often just a bug, operator precedence logic errors can have serious consequences if they are used in security-critical code, such as making an authentication decision.

##Mitigation:


PHASE:Implementation:
Regularly wrap sub-expressions in parentheses, especially in security-critical code.

