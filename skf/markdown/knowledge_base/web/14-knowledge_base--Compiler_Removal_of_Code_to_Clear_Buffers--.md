## Description:

Sensitive memory is cleared according to the source code, but compiler optimizations leave the memory untouched when it is not read from again, aka dead store removal.

This compiler optimization error occurs when: 1. Secret data are stored in memory. 2. The secret data are scrubbed from memory by overwriting its contents. 3. The source code is compiled using an optimizing compiler, which identifies and removes the function that overwrites the contents as a dead store because the memory is not used subsequently.

## Mitigation:


PHASE:Implementation:
Store the sensitive data in a volatile memory location if available.

PHASE:Build and Compilation:
If possible, configure your compiler so that it does not remove dead stores.

PHASE:Architecture and Design:
Where possible, encrypt sensitive data that are used by a software system.

