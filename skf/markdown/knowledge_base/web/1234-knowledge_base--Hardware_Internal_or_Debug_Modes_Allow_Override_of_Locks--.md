## Description:

The product implements register lock bit protection features that may permit security sensitive controls to modify system configuration after the lock is set through internal modes or debug features.

In integrated circuits and hardware IPs, device configuration controls are commonly programmed after a device power reset by a trusted firmware or software module (e.g., BIOS/bootloader) and then locked from any further modification. This is commonly implemented using a trusted lock bit, which when set disables writes to a protected set of registers or address regions. The lock protection is intended to prevent modification of certain system configuration (e.g., memory/memory protection unit configuration). If debug features supported by hardware or internal modes/system states are supported in the hardware design, they may allow modification of the lock protection.

## Mitigation:


PHASE:Architecture and Design Implementation Testing:
Security Lock bit protections must be reviewed for any bypass/override modes supported. Any supported override modes either must be removed, or these modes should be protected using features like secure authenticated, authorized debug modes. Security lock programming flow and lock properties must be tested in pre-si, post-si testing.:EFFECTIVENESS:High

