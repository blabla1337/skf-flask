## Description:

The software calls a non-reentrant function in a concurrent context in which a competing code sequence (e.g. thread or signal handler) may have an opportunity to call the same function or otherwise influence its state.



## Mitigation:


PHASE:Implementation:
Use reentrant functions if available.

PHASE:Implementation:
Add synchronization to your non-reentrant function.

PHASE:Implementation:
In Java, use the ReentrantLock Class.

