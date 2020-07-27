##Description:

The software uses a function that accepts a format string as an argument, but the format string originates from an external source.

When an attacker can modify an externally-controlled format string, this can lead to buffer overflows, denial of service, or data representation problems. It should be noted that in some circumstances, such as internationalization, the set of format strings is externally controlled by design. If the source of these format strings is trusted (e.g. only contained in library files that are only modifiable by the system administrator), then the external control might not itself pose a vulnerability.

##Mitigation:


PHASE:Requirements:
Choose a language that is not subject to this flaw.

PHASE:Implementation:
Ensure that all format string functions are passed a static string which cannot be controlled by the user and that the proper number of arguments are always sent to that function as well. If at all possible, use functions that do not support the %n operator in format strings. [REF-116] [REF-117]

PHASE:Build and Compilation:
Heed the warnings of compilers and linkers, since they may alert you to improper usage.

