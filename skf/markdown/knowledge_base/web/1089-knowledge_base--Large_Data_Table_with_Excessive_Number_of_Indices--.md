##Description:

The software uses a large data table that contains an excessively large number of indices.

This issue can make the software perform more slowly. If the relevant code is reachable by an attacker, then this performance problem might introduce a vulnerability. While the interpretation of large data table and excessively large number of indices may vary for each product or developer, CISQ recommends a default threshold of 1000000 rows for a large table and a default threshold of 3 indices.

##Mitigation:
