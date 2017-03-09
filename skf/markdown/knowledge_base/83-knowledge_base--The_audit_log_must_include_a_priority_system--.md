# The audit log must include a priority system.
-------

## Description:

If the audit log does not contain a clear priority system it will be difficult to
prioritize different types of process failures.


## Solution:

Whenever the web-application is writing error messages to the error log then these need
to have a correct priority label. The labels that you can use are LOW, MEDIUM and HIGH.
These labels can then be used at a later moment in time for easy and quick analysing
capabilities of the log files.

You should also verify security logging controls provide the ability to log success and
particularly failure events that are identified as security-relevant.
