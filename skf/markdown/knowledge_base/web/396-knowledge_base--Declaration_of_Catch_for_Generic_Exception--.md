##Description:

Catching overly broad exceptions promotes complex error handling code that is more likely to contain security vulnerabilities.

Multiple catch blocks can get ugly and repetitive, but condensing catch blocks by catching a high-level class like Exception can obscure exceptions that deserve special treatment or that should not be caught at this point in the program. Catching an overly broad exception essentially defeats the purpose of Java's typed exceptions, and can become particularly dangerous if the program grows and begins to throw new types of exceptions. The new exception types will not receive any attention.

##Mitigation:
