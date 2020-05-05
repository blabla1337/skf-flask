## Description:

Truncation errors occur when a primitive is cast to a primitive of a smaller size and data is lost in the conversion.

When a primitive is cast to a smaller primitive, the high order bits of the large value are lost in the conversion, potentially resulting in an unexpected value that is not equal to the original value. This value may be required as an index into a buffer, a loop iterator, or simply necessary state data. In any case, the value cannot be trusted and the system will be in an undefined state. While this method may be employed viably to isolate the low bits of a value, this usage is rare, and truncation usually implies that an implementation error has occurred.

## Mitigation:


PHASE:Implementation:
Ensure that no casts, implicit or explicit, take place that move from a larger size primitive or a smaller size primitive.

