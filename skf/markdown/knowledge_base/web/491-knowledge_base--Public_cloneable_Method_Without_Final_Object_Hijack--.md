## Description:

A class has a cloneable() method that is not declared final, which allows an object to be created without calling the constructor. This can cause the object to be in an unexpected state.



## Mitigation:


PHASE:Implementation:
Make the cloneable() method final.

