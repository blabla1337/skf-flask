## Description:

The product incorrectly implements register lock bit protection features such that protected controls can be programmed even after the lock has been set.

In integrated circuits and hardware IPs, device configuration controls are commonly programmed after a device power reset by a trusted firmware or software module (e.g., BIOS/bootloader) and then locked from any further modification. This is commonly implemented using a trusted lock bit, which when set disables writes to a protected set of registers or address regions. Design or coding errors in the implementation of the lock bit protection feature may allow the lock bit to be modified or cleared by software after being set to unlock the system.

## Mitigation:


PHASE:Architecture and Design Implementation Testing:
Security lock bit protections must be reviewed for design inconsistency and common weaknesses. Security lock programming flow and lock properties must be tested in pre-silicon, post-silicon testing.:EFFECTIVENESS:High

