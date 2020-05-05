## Description:

A NULL pointer dereference occurs when the application dereferences a pointer that it expects to be valid, but is NULL, typically causing a crash or exit.

NULL pointer dereference issues can occur through a number of flaws, including race conditions, and simple programming omissions.

## Mitigation:


PHASE:Implementation:
If all pointers that could have been modified are sanity-checked previous to use, nearly all NULL pointer dereferences can be prevented.

PHASE:Requirements:
The choice could be made to use a language that is not susceptible to these issues.

PHASE:Implementation:
Check the results of all functions that return a value and verify that the value is non-null before acting upon it.:EFFECTIVENESS:Moderate

PHASE:Architecture and Design:
Identify all variables and data stores that receive information from external sources, and apply input validation to make sure that they are only initialized to expected values.

PHASE:Implementation:
Explicitly initialize all your variables and other data stores, either during declaration or just before the first usage.

PHASE:Testing:
Use automated static analysis tools that target this type of weakness. Many modern techniques use data flow analysis to minimize the number of false positives. This is not a perfect solution, since 100% accuracy and coverage are not feasible.

