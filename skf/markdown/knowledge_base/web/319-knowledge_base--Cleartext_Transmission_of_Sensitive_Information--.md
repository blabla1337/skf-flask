## Description:

The software transmits sensitive or security-critical data in cleartext in a communication channel that can be sniffed by unauthorized actors.

Many communication channels can be sniffed by attackers during data transmission. For example, network traffic can often be sniffed by any attacker who has access to a network interface. This significantly lowers the difficulty of exploitation by attackers.

## Mitigation:


PHASE:Architecture and Design:
Encrypt the data with a reliable encryption scheme before transmitting.

PHASE:Implementation:
When using web applications with SSL, use SSL for the entire session from login to logout, not just for the initial login page.

PHASE:Testing:
Use tools and techniques that require manual (human) analysis, such as penetration testing, threat modeling, and interactive tools that allow the tester to record and modify an active session. These may be more effective than strictly automated techniques. This is especially the case with weaknesses that are related to design and business rules.

PHASE:Operation:
Configure servers to use encrypted channels for communication, which may include SSL or other secure protocols.

