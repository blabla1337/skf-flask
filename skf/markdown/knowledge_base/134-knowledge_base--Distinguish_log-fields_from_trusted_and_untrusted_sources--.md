# Distinguish log-fields from trusted and untrusted sources
-------

## Description:

Whenever log fields are distinguished from each other by means of logs from trusted and
untrusted log fields in your log entries your logs become clearer and more transparent.


## Solution:

Verify that log fields from trusted and untrusted sources are distinguishable in
log entries. If possible it is highly recommended that you separate these files
entirely from each other so the logs with untrusted user-input cannot corrupt the
system generated logs.

Recommended knowledge base items:

- Logging implemented on the server side
- Log injection
- The audit log must include a priority system
- User credentials in audit logs
- Logging guidelines
