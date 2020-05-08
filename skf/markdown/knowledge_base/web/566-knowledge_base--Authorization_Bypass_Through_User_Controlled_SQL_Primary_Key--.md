## Description:

The software uses a database table that includes records that should not be accessible to an actor, but it executes a SQL statement with a primary key that can be controlled by that actor.

When a user can set a primary key to any value, then the user can modify the key to point to unauthorized records. Database access control errors occur when: Data enters a program from an untrusted source. The data is used to specify the value of a primary key in a SQL query. The untrusted source does not have the permissions to be able to access all rows in the associated table.

## Mitigation:


PHASE:Implementation:
Assume all input is malicious. Use a standard input validation mechanism to validate all input for length, type, syntax, and business rules before accepting the data. Use an accept known good validation strategy.

PHASE:Implementation:
Use a parameterized query AND make sure that the accepted values conform to the business rules. Construct your SQL statement accordingly.

