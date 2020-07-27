##Description:

A public or protected static final field references a mutable object, which allows the object to be changed by malicious code, or accidentally from another package.



##Mitigation:


PHASE:Implementation:
Protect mutable objects by making them private. Restrict access to the getter and setter as well.

