##Description:

The software contains a client with a function or method that contains a large number of data accesses/queries that are sent through a data manager, i.e., does not use efficient database capabilities.

This issue can make the software perform more slowly. If the relevant code is reachable by an attacker, then this performance problem might introduce a vulnerability. While the interpretation of large number of data accesses/queries may vary for each product or developer, CISQ recommends a default maximum of 2 data accesses per function/method.

##Mitigation:
