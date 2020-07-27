##Description:

The software uses a data element that has an excessively large number of sub-elements with non-primitive data types such as structures or aggregated objects.

This issue can make the software perform more slowly. If the relevant code is reachable by an attacker, then this performance problem might introduce a vulnerability. While the interpretation of excessively large may vary for each product or developer, CISQ recommends a default of 5 sub-elements.

##Mitigation:
