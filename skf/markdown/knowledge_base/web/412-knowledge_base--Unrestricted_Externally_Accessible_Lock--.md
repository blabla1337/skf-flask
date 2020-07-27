##Description:

The software properly checks for the existence of a lock, but the lock can be externally controlled or influenced by an actor that is outside of the intended sphere of control.

This prevents the software from acting on associated resources or performing other behaviors that are controlled by the presence of the lock. Relevant locks might include an exclusive lock or mutex, or modifying a shared resource that is treated as a lock. If the lock can be held for an indefinite period of time, then the denial of service could be permanent.

##Mitigation:


PHASE:Architecture and Design Implementation:
Use any access control that is offered by the functionality that is offering the lock.

PHASE:Architecture and Design Implementation:
Use unpredictable names or identifiers for the locks. This might not always be possible or feasible.

PHASE:Architecture and Design:
Consider modifying your code to use non-blocking synchronization methods.

