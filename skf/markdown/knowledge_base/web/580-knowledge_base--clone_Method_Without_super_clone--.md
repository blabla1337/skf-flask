## Description:

The software contains a clone() method that does not call super.clone() to obtain the new object.

All implementations of clone() should obtain the new object by calling super.clone(). If a class does not follow this convention, a subclass's clone() method will return an object of the wrong type.

## Mitigation:


PHASE:Implementation:
Call super.clone() within your clone() method, when obtaining a new object.

PHASE:Implementation:
In some cases, you can eliminate the clone method altogether and use copy constructors.

