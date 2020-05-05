## Description:

The chip includes chicken bits or undocumented features that can create entry points for unauthorized actors.

A common design practice is to use chicken bits, which are bits on a chip that can be used to disable certain functional security features. They can facilitate quick identification and isolation of faulty components, features that negatively affect performance, or features that do not provide the required controllability for debug and test. Another way to achieve this is through implementation of undocumented features. An attacker might exploit these interfaces for unauthorized access.

## Mitigation:


PHASE:Architecture and Design Implementation:
Do not implement chicken bits. If implemented, ensure that they are disabled in production devices. Document all interfaces to the chip.:EFFECTIVENESS:High

