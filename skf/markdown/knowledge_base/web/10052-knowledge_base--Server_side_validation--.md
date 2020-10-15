##Description:

Validation of user supplied input must always be enforced on the server side.
Whenever validation of the input is being perfomed on the client side then
the constraints can easilly be bypassed whenever an attacker uses an intercepting proxy
which he can use to tamper data after they have been validated and send to the server. 

Or the attacker can simply change the constraint on the client side in his browser to bypass the 
constraints.

##Mitigation:

All validation of input should be handled on the server side. Whenever the validation is handled on 
the server side, the validation logic is outside of the scope of the attacker and he can not influence
the results.

Note: Validation of input should never be done with a black-listing aproach since attackers can be very
nifty in bypassing these type of constraints. Always perform white list validation checks preferably in
combination on type checking. i.e if the application expects the value to be an integer, do not make
the application accept a value of a string. This input should be logged and rejected.
