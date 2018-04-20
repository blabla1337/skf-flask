## Description:

The logging should contain some guidelines in order to organize your logging file in such
a way it  would allow for a detailed investigation of the timeline when an event happens.

## Solution:

The logging file should at least contain, a timestamp from a reliable source, severity
level of the event, an indication that this is a security relevant event
(if mixed with other logs), the identity of the user that caused the event
(if there is a user associated with the event), the source IP address of the request
associated with the event, whether the event succeeded or failed, and a
description of the event. Also verify that log fields from trusted and untrusted sources
are distinguishable in log entries, preferably stored in different files so they cannot
taint each other whenever log injection occurs.

Verify accessing sensitive data is logged, if the data is collected under relevant data protection
directives or where logging of accesses is required.
