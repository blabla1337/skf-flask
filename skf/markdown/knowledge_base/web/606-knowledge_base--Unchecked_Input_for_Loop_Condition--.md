## Description:

The product does not properly check inputs that are used for loop conditions, potentially leading to a denial of service because of excessive looping.



## Mitigation:


PHASE:Implementation:
Do not use user-controlled data for loop conditions.

PHASE:Implementation:
Perform input validation.

