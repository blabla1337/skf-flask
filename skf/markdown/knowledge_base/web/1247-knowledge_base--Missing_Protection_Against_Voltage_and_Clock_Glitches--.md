##Description:

The product does not contain the necessary additional circuitry or sensors to detect and mitigate voltage and clock glitches.

A product might support security features such as secure boot that are supported through hardware and firmware implementation. This involves establishing a chain of trust, starting with an immutable root of trust by checking the signature of the next stage (culminating with the OS and runtime software) against a golden value before transferring control. The intermediate stages typically set up the system in a secure state by configuring several access control settings. Similarly, any password-checking logic for exercising the debug interface, etc. can implemented in hardware, firmware, or both. This implementation needs to be robust against fault attacks such as voltage glitches and clock glitches that an attacker may leverage to compromise the system.

##Mitigation:


PHASE:Architecture and Design Implementation:
At the circuit-level, using Tunable Replica Circuits (TRCs) or special flip-flops such as Razor flip-flops helps mitigate glitches. At SoC or platform level, level sensors can be implemented to detect glitches. Implementing redundancy in security-sensitive code (e.g., where checks are performed) helps in mitigating glitches.

