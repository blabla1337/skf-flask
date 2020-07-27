##Description:

The code calls sizeof() on a malloced pointer type, which always returns the wordsize/8. This can produce an unexpected result if the programmer intended to determine how much memory has been allocated.

The use of sizeof() on a pointer can sometimes generate useful information. An obvious case is to find out the wordsize on a platform. More often than not, the appearance of sizeof(pointer) indicates a bug.

##Mitigation:


PHASE:Implementation:
Use expressions such as sizeof(*pointer) instead of sizeof(pointer), unless you intend to run sizeof() on a pointer type to gain some platform independence or if you are allocating a variable on the stack.

