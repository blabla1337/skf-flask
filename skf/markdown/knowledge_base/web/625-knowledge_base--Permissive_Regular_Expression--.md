##Description:

The product uses a regular expression that does not sufficiently restrict the set of allowed values.

This effectively causes the regexp to accept substrings that match the pattern, which produces a partial comparison to the target. In some cases, this can lead to other weaknesses. Common errors include: not identifying the beginning and end of the target string using wildcards instead of acceptable character ranges others

##Mitigation:


PHASE:Implementation:
When applicable, ensure that the regular expression marks beginning and ending string patterns, such as /^string$/ for Perl.

