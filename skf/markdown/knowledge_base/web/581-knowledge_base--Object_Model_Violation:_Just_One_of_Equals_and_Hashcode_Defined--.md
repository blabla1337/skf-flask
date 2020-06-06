## Description:

The software does not maintain equal hashcodes for equal objects.

Java objects are expected to obey a number of invariants related to equality. One of these invariants is that equal objects must have equal hashcodes. In other words, if a.equals(b) == true then a.hashCode() == b.hashCode().

## Mitigation:


PHASE:Implementation:
Both Equals() and Hashcode() should be defined.

