## Description:

The software does not terminate or incorrectly terminates a string or array with a null character or equivalent terminator.

Null termination errors frequently occur in two different ways. An off-by-one error could cause a null to be written out of bounds, leading to an overflow. Or, a program could use a strncpy() function call incorrectly, which prevents a null terminator from being added at all. Other scenarios are possible.

## Mitigation:


PHASE:Requirements:
Use a language that is not susceptible to these issues. However, be careful of null byte interaction errors (CWE-626) with lower-level constructs that may be written in a language that is susceptible.

PHASE:Implementation:
Ensure that all string functions used are understood fully as to how they append null characters. Also, be wary of off-by-one errors when appending nulls to the end of strings.

PHASE:Implementation:
If performance constraints permit, special code can be added that validates null-termination of string buffers, this is a rather naive and error-prone solution.

PHASE:Implementation:
Switch to bounded string manipulation functions. Inspect buffer lengths involved in the buffer overrun trace reported with the defect.

PHASE:Implementation:
Add code that fills buffers with nulls (however, the length of buffers still needs to be inspected, to ensure that the non null-terminated string is not written at the physical end of the buffer).

