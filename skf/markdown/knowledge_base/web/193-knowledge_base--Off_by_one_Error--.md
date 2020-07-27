##Description:

A product calculates or uses an incorrect maximum or minimum value that is 1 more, or 1 less, than the correct value.



##Mitigation:


PHASE:Implementation:
When copying character arrays or using character manipulation methods, the correct size parameter must be used to account for the null terminator that needs to be added at the end of the array. Some examples of functions susceptible to this weakness in C include strcpy(), strncpy(), strcat(), strncat(), printf(), sprintf(), scanf() and sscanf().

