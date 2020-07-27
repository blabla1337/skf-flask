##Description:

The product does not implement or incorrectly handles the implementation of write operations in limited-write non-volatile memories.

Non-volatile memories such as NAND Flash, EEPROM, etc. have individually erasable segments, each of which can be put through a limited number of program/erase or write cycles. For example, the device can only endure a limited number of writes, after which the device becomes unreliable. In order to wear out the cells in a uniform manner, non-volatile memory and storage products based on the above-mentioned technologies implement a technique called wear leveling. Once a set threshold is reached, wear leveling maps writes of a logical block to a different physical block. This prevents a single physical block from prematurely failing due to a high concentration of writes. If wear leveling is improperly implemented, attackers can execute a write virus and cause the storage to become unreliable much faster than the minimally guaranteed platform lifetime.

##Mitigation:


PHASE:Architecture and Design Implementation Testing:
Include secure wear leveling algorithms and ensure that it cannot be bypassed by known write viruses.:EFFECTIVENESS:High

