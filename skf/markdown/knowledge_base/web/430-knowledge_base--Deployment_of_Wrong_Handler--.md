##Description:

The wrong handler is assigned to process an object.

An example of deploying the wrong handler would be calling a servlet to reveal source code of a .JSP file, or automatically determining type of the object even if it is contradictory to an explicitly specified type.

##Mitigation:


PHASE:Architecture and Design:
Perform a type check before interpreting an object.

PHASE:Architecture and Design:
Reject any inconsistent types, such as a file with a .GIF extension that appears to consist of PHP code.

