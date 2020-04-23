## Description:

The reserved bits in a hardware design are not disabled prior to production. Typically, reserved bits are used for future capabilities and should not support any functional logic in the design. However, designers might covertly use these bits to debug or further develop new capabilities in production hardware. Adversaries with access to these bits will write to them in hopes of compromising hardware state.

Reserved bits are labeled as such so they can be allocated for a later purpose. They are not to do anything in the current design. However, designers might want to use these bits to debug or control/configure a future capability to help minimize time to market (TTM). If the logic being controlled by these bits is still enabled in production, an adversary could use the logic to induce unwanted/unsupported behavior in the hardware.

## Mitigation:


PHASE:Architecture and Design Implementation:
Include a feature disable

PHASE:Integration:
Any writes to these reserve bits are blocked (e.g., ignored, access-protected, etc.), or an exception can be asserted.

