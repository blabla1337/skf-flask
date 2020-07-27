##Description:

The product implements register lock bit protection features with the intent to disable changes to system configuration after the lock is set. Some of the protected registers or lock bits become programmable after power state transitions (e.g., Entry and wake from low power sleep modes).

Integrated circuits and hardware IPs can expose the device configuration controls that need to be programmed after device power reset by a trusted firmware or software module (commonly set by BIOS/bootloader) and then locked from any further modification. In hardware design this is commonly implemented using a programmable lock bit, which when set disables writes to a protected set of registers or address regions. Some common weaknesses that can exist in such a protection scheme is that the lock gets cleared, the values of the protected registers get reset, or the lock become programmable after a power state transition.

##Mitigation:


PHASE:Architecture and Design Implementation Testing:
Security Lock bit protections must be reviewed for behavior across supported power state transitions. Security lock programming flow and lock properties must be tested in pre-si, post-si testing, including testing these across power transitions.:EFFECTIVENESS:High

