##Description:

The software accesses a data resource through a database without using a connection pooling capability.

This issue can make the software perform more slowly, as connection pools allow connections to be reused without the overhead and time consumption of opening and closing a new connection. If the relevant code is reachable by an attacker, then this performance problem might introduce a vulnerability.

##Mitigation:
