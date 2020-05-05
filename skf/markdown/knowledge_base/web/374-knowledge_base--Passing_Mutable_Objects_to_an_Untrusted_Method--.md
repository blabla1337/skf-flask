## Description:

The program sends non-cloned mutable data as an argument to a method or function.

The function or method that has been called can alter or delete the mutable data. This could violate assumptions that the calling function has made about its state. In situations where unknown code is called with references to mutable data, this external code could make changes to the data sent. If this data was not previously cloned, the modified data might not be valid in the context of execution.

## Mitigation:


PHASE:Implementation:
Pass in data which should not be altered as constant or immutable.

PHASE:Implementation:
Clone all mutable data before passing it into an external function . This is the preferred mitigation. This way, regardless of what changes are made to the data, a valid copy is retained for use by the class.

