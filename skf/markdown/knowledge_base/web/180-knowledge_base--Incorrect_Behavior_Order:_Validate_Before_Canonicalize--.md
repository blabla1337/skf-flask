##Description:

The software validates input before it is canonicalized, which prevents the software from detecting data that becomes invalid after the canonicalization step.

This can be used by an attacker to bypass the validation and launch attacks that expose weaknesses that would otherwise be prevented, such as injection.

##Mitigation:


PHASE:Implementation:STRATEGY:Input Validation:
Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass whitelist validation schemes by introducing dangerous inputs after they have been checked.

