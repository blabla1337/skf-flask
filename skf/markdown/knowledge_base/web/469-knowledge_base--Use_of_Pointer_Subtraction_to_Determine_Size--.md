##Description:

The application subtracts one pointer from another in order to determine size, but this calculation can be incorrect if the pointers do not exist in the same memory chunk.



##Mitigation:


PHASE:Implementation:
Save an index variable. This is the recommended solution. Rather than subtract pointers from one another, use an index variable of the same size as the pointers in question. Use this variable to walk from one pointer to the other and calculate the difference. Always sanity check this number.

