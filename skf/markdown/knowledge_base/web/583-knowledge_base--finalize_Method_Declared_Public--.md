## Description:

The program violates secure coding principles for mobile code by declaring a finalize() method public.

A program should never call finalize explicitly, except to call super.finalize() inside an implementation of finalize(). In mobile code situations, the otherwise error prone practice of manual garbage collection can become a security threat if an attacker can maliciously invoke a finalize() method because it is declared with public access.

## Mitigation:


PHASE:Implementation:
If you are using finalize() as it was designed, there is no reason to declare finalize() with anything other than protected access.

