##Description:

The product has a method that is declared public, but returns a reference to a private data structure, which could then be modified in unexpected ways.



##Mitigation:


PHASE:Implementation:
Declare the method private.

PHASE:Implementation:
Clone the member data and keep an unmodified version of the data private to the object.

PHASE:Implementation:
Use public setter methods that govern how a private member can be modified.

