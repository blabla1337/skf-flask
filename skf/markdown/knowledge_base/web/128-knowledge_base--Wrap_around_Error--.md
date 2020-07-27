##Description:

Wrap around errors occur whenever a value is incremented past the maximum value for its type and therefore wraps around to a very small, negative, or undefined value.



##Mitigation:


PHASE

DESCRIPTION:Requirements specification: The choice could be made to use a language that is not susceptible to these issues.

PHASE:Architecture and Design:
Provide clear upper and lower bounds on the scale of any protocols designed.

PHASE:Implementation:
Place sanity checks on all incremented variables to ensure that they remain within reasonable bounds.

