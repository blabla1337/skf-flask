## Description:

The software properly neutralizes certain special elements, but it improperly neutralizes equivalent special elements.

The software may have a fixed list of special characters it believes is complete. However, there may be alternate encodings, or representations that also have the same meaning. For example, the software may filter out a leading slash (/) to prevent absolute path names, but does not account for a tilde (~) followed by a user name, which on some *nix systems could be expanded to an absolute pathname. Alternately, the software might filter a dangerous -e command-line switch when calling an external program, but it might not account for --exec or other switches that have the same semantics.

## Mitigation:


PHASE:Requirements:
Programming languages and supporting technologies might be chosen which are not subject to these issues.

PHASE:Implementation:
Utilize an appropriate mix of whitelist and blacklist parsing to filter equivalent special element syntax from all input.

