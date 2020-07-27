##Description:

The product exposes security-sensitive values stored in fuses during debug.

Several security-sensitive values are blown as fuses in a chip to be used during early-boot flows or later at runtime. Examples of these security-sensitive values include root keys, encryption keys, manufacturing-specific information, chip-manufacturer-specific information, and original-equipment-manufacturer (OEM) data. After the chip is powered on, these values are sensed from fuses and stored in temporary locations such as registers and local memories. These locations are typically access-control protected from untrusted agents capable of accessing them. Even to trusted agents, only read-access is provided. However, these locations are not blocked during debug flows, allowing an untrusted debugger to access these assets and compromise system security.

##Mitigation:


PHASE:Architecture and Design Implementation:
When in debug mode, disable access to security-sensitive values sensed from fuses and stored in temporary locations.

