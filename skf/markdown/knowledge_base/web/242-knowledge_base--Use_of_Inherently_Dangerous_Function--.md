## Description:

The program calls a function that can never be guaranteed to work safely.

Certain functions behave in dangerous ways regardless of how they are used. Functions in this category were often implemented without taking security concerns into account. The gets() function is unsafe because it does not perform bounds checking on the size of its input. An attacker can easily send arbitrarily-sized input to gets() and overflow the destination buffer. Similarly, the >> operator is unsafe to use when reading into a statically-allocated character array because it does not perform bounds checking on the size of its input. An attacker can easily send arbitrarily-sized input to the >> operator and overflow the destination buffer.

## Mitigation:


PHASE:Implementation Requirements:
Ban the use of dangerous functions. Use their safe equivalent.

PHASE:Testing:
Use grep or static analysis tools to spot usage of dangerous functions.

