##Description:

The software contains a method that accesses an object but does not later invoke the element's associated finalize/destructor method.

This issue can make the software perform more slowly by retaining memory and/or other resources longer than necessary. If the relevant code is reachable by an attacker, then this performance problem might introduce a vulnerability.

##Mitigation:
