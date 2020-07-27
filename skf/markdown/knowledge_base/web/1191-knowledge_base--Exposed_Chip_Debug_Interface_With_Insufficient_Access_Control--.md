##Description:

The chip does not implement or does not correctly enforce access control on the debug interface, thus allowing an attacker to exercise the debug interface to access a portion of the chip internal registers that typically would not be exposed.

Integrated circuits can expose the chip internals through a scan chain interconnected through internal registers etc., through scan flip-flops. A Joint Test Action Group (JTAG) compatible test access port usually provides access to this scan chain for debugging the chip. Since almost every asset in the chip can be accessed over this debug interface, chip manufacturers typically insert some form of password-based or challenge-response based access control mechanisms to prevent misuse. This mechanism is implemented in addition to on-chip protections that are already present. If this debug access control is not implemented or the access control check is not implemented properly, or if the hardware does not clear secret keys, etc., when debug more is entered, an attacker may be able to bypass on-chip access control mechanisms through debug features/interfaces.

##Mitigation:


PHASE:Architecture and Design:STRATEGY:Separation of Privilege:
Implement an access control mechanism to exercise the debug interface in order to control and observe security-sensitive chip internals. Password checking logic should be resistant to timing attacks. Security-sensitive data stored in registers, such as keys, etc. should be cleared when entering debug mode.

