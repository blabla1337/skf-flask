##Description:

The code does not explicitly delimit a block that is intended to contain 2 or more statements, creating a logic error.

In some languages, braces (or other delimiters) are optional for blocks. When the delimiter is omitted, it is possible to insert a logic error in which a statement is thought to be in a block but is not. In some cases, the logic error can have security implications.

##Mitigation:


PHASE:Implementation:
Always use explicit block delimitation and use static-analysis technologies to enforce this practice.

