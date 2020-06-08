## Description:

The software validates data before it has been filtered, which prevents the software from detecting data that becomes invalid after the filtering step.

This can be used by an attacker to bypass the validation and launch attacks that expose weaknesses that would otherwise be prevented, such as injection.

## Mitigation:


PHASE:Implementation Architecture and Design:
Inputs should be decoded and canonicalized to the application's current internal representation before being filtered.

