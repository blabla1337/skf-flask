## Description:

Runtime Integrity Checks

MSTG-RESILIENCE-6: The app detects, and responds to, tampering the code and data in its own memory space.

Controls in this category verify the integrity of the app's memory space to defend the app against memory patches applied during runtime. Such patches include unwanted changes to binary code, bytecode, function pointer tables, and important data structures, as well as rogue code loaded into process memory. Integrity can be verified by:
	1. comparing the contents of memory or a checksum over the contents to good values,
	2. searching memory for the signatures of unwanted modifications.


## Mitigation:

Implement proper runtime integrity control. 