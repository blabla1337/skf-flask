# Sanitize sensitive data rapidly from memory
-------

## Description:

Whenever sensitive data is rapidly removed from the systems memory, this decreases the
possibility the attacker can compromise this data by means of memory dumping attacks.


## Solution:

Verify that sensitive data is rapidly sanitized from memory as soon as it is no longer
needed and handled in accordance to functions and techniques supported by the
framework/library/operating system.
