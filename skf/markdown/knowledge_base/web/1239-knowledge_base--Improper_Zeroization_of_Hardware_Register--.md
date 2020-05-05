## Description:

The hardware product does not properly clear sensitive information from built-in registers when the user of the hardware block changes.

Hardware logic operates on data stored in registers local to the hardware block. Most hardware IPs, including cryptographic accelerators, rely on registers to buffer I/O, store intermediate values, and interface with software. The result of this is that sensitive information, such as passwords or encryption keys, can exist in locations not transparent to the user of the hardware logic. When a different entity obtains access to the IP due to a change in operating mode or conditions, the new entity can extract information belonging to the previous user if no mechanisms are in place to clear register contents. It is important to clear information stored in the hardware if a physical attack on the product is detected, or if the user of the hardware block changes. The process of clearing register contents in a hardware IP is referred to as zeroization in standards for cryptographic hardware modules such as FIPS-140-2 [REF-267].

## Mitigation:


PHASE:Architecture and Design:
Every register potentially containing sensitive information must have a policy specifying how and when information is cleared, in addition to clarifying if it is the responsibility of the hardware logic or IP user to initiate the zeroization procedure at the appropriate time.

