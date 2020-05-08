## Description:

The software checks the state of a resource before using that resource, but the resource's state can change between the check and the use in a way that invalidates the results of the check. This can cause the software to perform invalid actions when the resource is in an unexpected state.

This weakness can be security-relevant when an attacker can influence the state of the resource between check and use. This can happen with shared resources such as files, memory, or even variables in multithreaded programs.

## Mitigation:


PHASE:Implementation:
The most basic advice for TOCTOU vulnerabilities is to not perform a check before the use. This does not resolve the underlying issue of the execution of a function on a resource whose state and identity cannot be assured, but it does help to limit the false sense of security given by the check.

PHASE:Implementation:
When the file being altered is owned by the current user and group, set the effective gid and uid to that of the current user and group when executing this statement.

PHASE:Architecture and Design:
Limit the interleaving of operations on files from multiple processes.

PHASE:Implementation Architecture and Design:
If you cannot perform operations atomically and you must share access to the resource between multiple processes or threads, then try to limit the amount of time (CPU cycles) between the check and use of the resource. This will not fix the problem, but it could make it more difficult for an attack to succeed.

PHASE:Implementation:
Recheck the resource after the use call to verify that the action was taken appropriately.

PHASE:Architecture and Design:
Ensure that some environmental locking mechanism can be used to protect resources effectively.

PHASE:Implementation:
Ensure that locking occurs before the check, as opposed to afterwards, such that the resource, as checked, is the same as it is when in use.

