## Description:

An object contains a public static field that is not marked final, which might allow it to be modified in unexpected ways.

Public static variables can be read without an accessor and changed without a mutator by any classes in the application.

## Mitigation:


PHASE:Architecture and Design:
Clearly identify the scope for all critical data elements, including whether they should be regarded as static.

PHASE:Implementation:
Make any static fields private and constant. A constant field is denoted by the keyword 'const' in C/C++ and ' final' in Java

