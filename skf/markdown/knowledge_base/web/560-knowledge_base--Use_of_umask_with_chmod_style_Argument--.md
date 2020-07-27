##Description:

The product calls umask() with an incorrect argument that is specified as if it is an argument to chmod().



##Mitigation:


PHASE:Implementation:
Use umask() with the correct argument.

PHASE:Testing:
If you suspect misuse of umask(), you can use grep to spot call instances of umask().

