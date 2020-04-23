## Description:

The software does not initialize or incorrectly initializes a resource, which might leave the resource in an unexpected state when it is accessed or used.

This can have security implications when the associated resource is expected to have certain properties or values, such as a variable that determines whether a user has been authenticated or not.

## Mitigation:


PHASE:Requirements:STRATEGY:Language Selection:
Use a language that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, in Java, if the programmer does not explicitly initialize a variable, then the code could produce a compile-time error (if the variable is local) or automatically initialize the variable to the default value for the variable's type. In Perl, if explicit initialization is not performed, then a default value of undef is assigned, which is interpreted as 0, false, or an equivalent value depending on the context in which the variable is accessed.

PHASE:Architecture and Design:
Identify all variables and data stores that receive information from external sources, and apply input validation to make sure that they are only initialized to expected values.

PHASE:Implementation:
Explicitly initialize all your variables and other data stores, either during declaration or just before the first usage.

PHASE:Implementation:
Pay close attention to complex conditionals that affect initialization, since some conditions might not perform the initialization.

PHASE:Implementation:
Avoid race conditions (CWE-362) during initialization routines.

PHASE:Build and Compilation:
Run or compile your software with settings that generate warnings about uninitialized variables or data.

PHASE:Testing:
Use automated static analysis tools that target this type of weakness. Many modern techniques use data flow analysis to minimize the number of false positives. This is not a perfect solution, since 100% accuracy and coverage are not feasible.

