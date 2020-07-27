##Description:

The software initializes critical internal variables or data stores using inputs that can be modified by untrusted actors.

A software system should be reluctant to trust variables that have been initialized outside of its trust boundary, especially if they are initialized by users. The variables may have been initialized incorrectly. If an attacker can initialize the variable, then they can influence what the vulnerable system will do.

##Mitigation:


PHASE:Implementation:STRATEGY:Input Validation:
A software system should be reluctant to trust variables that have been initialized outside of its trust boundary. Ensure adequate checking (e.g. input validation) is performed when relying on input from outside a trust boundary.

PHASE:Architecture and Design:
Avoid any external control of variables. If necessary, restrict the variables that can be modified using a whitelist, and use a different namespace or naming convention if possible.

