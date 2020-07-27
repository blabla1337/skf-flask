##Description:

Sending non-cloned mutable data as a return value may result in that data being altered or deleted by the calling function.

In situations where functions return references to mutable data, it is possible that the external code which called the function may make changes to the data sent. If this data was not previously cloned, the class will then be using modified data which may violate assumptions about its internal state.

##Mitigation:


PHASE:Implementation:
Declare returned data which should not be altered as constant or immutable.

PHASE:Implementation:
Clone all mutable data before returning references to it. This is the preferred mitigation. This way, regardless of what changes are made to the data, a valid copy is retained for use by the class.

