## Description:

The product uses the wrong operator when comparing a string, such as using == when the equals() method should be used instead.

In Java, using == or != to compare two strings for equality actually compares two objects for equality, not their values. Chances are good that the two references will never be equal. While this weakness often only affects program correctness, if the equality is used for a security decision, it could be leveraged to affect program security.

## Mitigation:


PHASE:Implementation:
Use equals() to compare strings.:EFFECTIVENESS:High

