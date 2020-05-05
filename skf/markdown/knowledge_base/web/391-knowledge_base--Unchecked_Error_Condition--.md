## Description:

[PLANNED FOR DEPRECATION. SEE MAINTENANCE NOTES.] Ignoring exceptions and other error conditions may allow an attacker to induce unexpected behavior unnoticed.



## Mitigation:


PHASE:Requirements:
The choice between a language which has named or unnamed exceptions needs to be done. While unnamed exceptions exacerbate the chance of not properly dealing with an exception, named exceptions suffer from the up call version of the weak base class problem.

PHASE:Requirements:
A language can be used which requires, at compile time, to catch all serious exceptions. However, one must make sure to use the most current version of the API as new exceptions could be added.

PHASE:Implementation:
Catch all relevant exceptions. This is the recommended solution. Ensure that all exceptions are handled in such a way that you can be sure of the state of your system at any given moment.

