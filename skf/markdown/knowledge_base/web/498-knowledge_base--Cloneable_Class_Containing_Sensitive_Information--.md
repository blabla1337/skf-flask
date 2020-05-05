## Description:

The code contains a class with sensitive data, but the class is cloneable. The data can then be accessed by cloning the class.

Cloneable classes are effectively open classes, since data cannot be hidden in them. Classes that do not explicitly deny cloning can be cloned by any other class without running the constructor.

## Mitigation:


PHASE:Implementation:
If you do make your classes clonable, ensure that your clone method is final and throw super.clone().

