##Description:

The software does not properly prevent access to, or detect usage of, alternate data streams (ADS).

An attacker can use an ADS to hide information about a file (e.g. size, the name of the process) from a system or file browser tools such as Windows Explorer and 'dir' at the command line utility. Alternately, the attacker might be able to bypass intended access restrictions for the associated data fork.

##Mitigation:


PHASE:Testing:
Software tools are capable of finding ADSs on your system.

PHASE:Implementation:
Ensure that the source code correctly parses the filename to read or write to the correct stream.

