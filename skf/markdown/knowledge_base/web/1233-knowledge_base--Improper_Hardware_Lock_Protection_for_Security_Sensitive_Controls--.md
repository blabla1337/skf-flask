## Description:

The product implements a register lock bit protection feature that permits security sensitive controls to modify the protected configuration.

Integrated circuits and hardware IPs can expose the device configuration controls that need to be programmed after device power reset by a trusted firmware or software module (commonly set by BIOS/bootloader) and then locked from any further modification. This is commonly implemented using a trusted lock bit, which when set disables writes to a protected set of registers or address regions. The lock protection is intended to prevent modification of certain system configuration (e.g., memory/memory protection unit configuration). If any system registers/controls that can modify the protected configuration are not write-protected by the lock, they can then be leveraged by software to modify the protected configuration.

## Mitigation:


PHASE:Architecture and Design Implementation Testing:
Security lock bit protections must be reviewed for design inconsistency and common weaknesses. Security lock bit protections must be reviewed common weaknesses. Security lock programming flow and lock properties must be tested in pre-si, post-si testing.

