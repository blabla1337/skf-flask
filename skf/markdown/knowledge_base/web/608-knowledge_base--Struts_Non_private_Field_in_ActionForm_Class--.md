## Description:

An ActionForm class contains a field that has not been declared private, which can be accessed without using a setter or getter.



## Mitigation:


PHASE:Implementation:
Make all fields private. Use getter to get the value of the field. Setter should be used only by the framework; setting an action form field from other actions is bad practice and should be avoided.

