
Input validation
-------

**Description:**

To ensure that the application is robust against all forms of input data, this data should 
be sanitised and/or encoded server-side since an attacker could otherwise easy bypass 
these checks with an intercepting proxy.

**Solution:**

All input validation and encoding-routines should be implemented on the server-side 
outside the reach of an attacker. Just as with the input rejection you should make sure that
after validating the user-input, whenever the input is bad it actually rejects, sanitises 
or formats your user-input into not malicious data. 

The recommended method for validating user input would be the positive validation method.
White-list input validation means allowing only input that is explicitly defined as valid,
as opposed to black-list input validation, which filters out known bad input.

You must also keep track of the users movements by adding an audit trail as well as an
counter for tracking the number of his violations(submitting bad input) in your input 
validation class. You should enforce a lockout whenever a unreasonable number of 
violations are detected by your application in order to protect it from attackers.

Also verify that structured data is strongly typed and validated against a defined schema 
including allowed characters, length and pattern (e.g. credit card numbers or telephone, 
or validating that two related fields are reasonable, such as validating suburbs and zip 
or post codes match).

This also goes for whenever you are expecting just an integer or alphanumeric values etc.
Every detection of input outside of the intended operation of the application should be 
logged and rejected by your application. 

Note: All this validation and rejection should always be performed on the server side.

Recommended knowledge base items:

- Positive validation method
- Input rejection
- Client side validation
- Single input validation controls

