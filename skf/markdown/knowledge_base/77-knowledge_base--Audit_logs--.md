# Audit logs
-------

## Description:

An audit trail (also called audit log) is a security-relevant chronological record,
set of records, and/or destination and source of records that provide documentary
evidence of the sequence of activities that have affected at any time a specific operation,
procedure, or event.

## Solution:

An audit log should contain the following items:

- User ID
- Operation
- Success/failure of the operation
- Privileges
- Timestamp

Depending on the gravity of the users violation, there should also be a record kept for
each user to lock their accounts after a certain number of violations. This should be
applied since we can now assume it is an attacker trying to compromise your application.

Also when doing audit logs, make sure you always do logging before taking action in case the
action is not properly processed or terminated by your application. When using this
approach you are always in possession of an complete audit trail.
