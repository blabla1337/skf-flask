## Description:

The software performs a comparison that only examines a portion of a factor before determining whether there is a match, such as a substring, leading to resultant weaknesses.

For example, an attacker might succeed in authentication by providing a small password that matches the associated portion of the larger, correct password.

## Mitigation:


PHASE:Testing:
Thoroughly test the comparison scheme before deploying code into production. Perform positive testing as well as negative testing.

