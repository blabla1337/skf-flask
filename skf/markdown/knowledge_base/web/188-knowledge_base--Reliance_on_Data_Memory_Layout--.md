##Description:

The software makes invalid assumptions about how protocol data or memory is organized at a lower level, resulting in unintended program behavior.

When changing platforms or protocol versions, in-memory organization of data may change in unintended ways. For example, some architectures may place local variables A and B right next to each other with A on top; some may place them next to each other with B on top; and others may add some padding to each. The padding size may vary to ensure that each variable is aligned to a proper word size. In protocol implementations, it is common to calculate an offset relative to another field to pick out a specific piece of data. Exceptional conditions, often involving new protocol versions, may add corner cases that change the data layout in an unusual way. The result can be that an implementation accesses an unintended field in the packet, treating data of one type as data of another type.

##Mitigation:


PHASE:Implementation Architecture and Design:
In flat address space situations, never allow computing memory addresses as offsets from another memory address.

PHASE:Architecture and Design:
Fully specify protocol layout unambiguously, providing a structured grammar (e.g., a compilable yacc grammar).

PHASE:Testing:
Testing: Test that the implementation properly handles each case in the protocol grammar.

