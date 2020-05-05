## Description:

The program compares classes by name, which can cause it to use the wrong class when multiple classes can have the same name.

If the decision to trust the methods and data of an object is based on the name of a class, it is possible for malicious users to send objects of the same name as trusted classes and thereby gain the trust afforded to known classes and types.

## Mitigation:


PHASE:Implementation:
Use class equivalency to determine type. Rather than use the class name to determine if an object is of a given type, use the getClass() method, and == operator.

