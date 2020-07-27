##Description:

The software is intended to manage data access through a particular data manager component such as a relational or non-SQL database, but it contains code that performs data access operations without using that component.

When the software has a data access component, the design may be intended to handle all data access operations through that component. If a data access operation is performed outside of that component, then this may indicate a violation of the intended design. This issue can prevent the software from running reliably. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability.

##Mitigation:
