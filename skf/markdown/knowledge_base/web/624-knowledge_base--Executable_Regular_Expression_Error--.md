##Description:

The product uses a regular expression that either (1) contains an executable component with user-controlled inputs, or (2) allows a user to enable execution by inserting pattern modifiers.

Case (2) is possible in the PHP preg_replace() function, and possibly in other languages when a user-controlled input is inserted into a string that is later parsed as a regular expression.

##Mitigation:


PHASE:Implementation:
The regular expression feature in some languages allows inputs to be quoted or escaped before insertion, such as Q and E in Perl.

