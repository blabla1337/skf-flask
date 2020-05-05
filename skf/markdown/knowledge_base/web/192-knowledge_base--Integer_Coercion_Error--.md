## Description:

Integer coercion refers to a set of flaws pertaining to the type casting, extension, or truncation of primitive data types.

Several flaws fall under the category of integer coercion errors. For the most part, these errors in and of themselves result only in availability and data integrity issues. However, in some circumstances, they may result in other, more complicated security related flaws, such as buffer overflow conditions.

## Mitigation:


PHASE:Requirements:
A language which throws exceptions on ambiguous data casts might be chosen.

PHASE:Architecture and Design:
Design objects and program flow such that multiple or complex casts are unnecessary

PHASE:Implementation:
Ensure that any data type casting that you must used is entirely understood in order to reduce the plausibility of error in use.

