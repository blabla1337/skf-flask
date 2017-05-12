# Client side constraints
-------

## Description:

Whenever constraints that are imposed on the client side are not enforced on the server side than
these constraints can be easilly bypassed by means of an intercepting proxy. i.e whenever user should not 
be able to edit a form by solely disabeling the input fields, a potential attacker can edit these input 
fields on the client side as editable and stil submit the form.

The same principle goes for whenever certain parts of the application should be inaccessible. Simply hiding
the pages from the presentation layer is insecure since the attacker can enumerate by brute forcing or
fuzzing himself into different pages. Again the access controls should be enforced also on the server side.  

## Solution:

All critical decision making logic must be enforced on the server side out of scope of a potential 
attacker. Client side constraints can be easilly bypassed.
