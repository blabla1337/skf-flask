##Description:

The software reads or writes to a buffer using an index or pointer that references a memory location after the end of the buffer.

This typically occurs when a pointer or its index is decremented to a position before the buffer; when pointer arithmetic results in a position before the buffer; or when a negative index is used, which generates a position before the buffer.

##Mitigation:
