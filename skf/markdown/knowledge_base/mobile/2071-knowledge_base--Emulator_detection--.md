## Description:

Emulator Detection

MSTG-RESILIENCE-5: The app detects, and responds to, being run in an emulator.

In the context of anti-reversing, the goal of emulator detection is to increase the difficulty of running the app on an emulated device, which impedes some tools and techniques reverse engineers like to use. This increased difficulty forces the reverse engineer to defeat the emulator checks or utilize the physical device, thereby barring the access required for large-scale device analysis.

However, this is not a concern on iOS. Only available simulator is the one that ships with Xcode. Simulator binaries are compiled to x86 code instead of ARM code and apps compiled for a real device (ARM architecture) don't run in the simulator. This makes the simulator useless for black box analysis and reverse engineering.


## Mitigation:

Implement a proper emulator detection mechanisms. 
