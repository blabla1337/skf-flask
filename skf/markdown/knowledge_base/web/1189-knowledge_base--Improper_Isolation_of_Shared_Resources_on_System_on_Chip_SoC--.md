##Description:

The product does not properly isolate shared resources between trusted and untrusted agents.

A System-On-Chip (SoC) has a lot of functionality, but may have a limited number of pins or pads. A pin can only perform one function at a time. However, it can be configured to perform multiple different functions. This technique is called pin multiplexing. Similarly, several resources on the chip may be shared to multiplex and support different features or functions. When such resources are shared between trusted and untrusted agents, untrusted agents may be able to access the assets intended to be accessed only by the trusted agents.

##Mitigation:


PHASE:Architecture and Design:STRATEGY:Separation of Privilege:
When sharing resources, avoid mixing agents of varying trust levels. Group untrusted agents together to access when sharing a resource. Similarly, group trusted agents (at same trust level).

