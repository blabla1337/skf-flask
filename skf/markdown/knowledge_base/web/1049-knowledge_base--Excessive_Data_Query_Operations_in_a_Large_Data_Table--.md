##Description:

The software performs a data query with a large number of joins and sub-queries on a large data table.

This issue can make the software perform more slowly. If the relevant code is reachable by an attacker, then this performance problem might introduce a vulnerability. While the interpretation of large data table and large number of joins or sub-queries may vary for each product or developer, CISQ recommends a default of 1 million rows for a large data table, a default minimum of 5 joins, and a default minimum of 3 sub-queries.

##Mitigation:
