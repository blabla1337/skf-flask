##Description:

A static code block creates an instance of a class.

This pattern identifies situations where a storable data element or member data element is initialized with a value in a block of code which is declared as static. This issue can make the software perform more slowly by performing initialization before it is needed. If the relevant code is reachable by an attacker, then this performance problem might introduce a vulnerability.

##Mitigation:
