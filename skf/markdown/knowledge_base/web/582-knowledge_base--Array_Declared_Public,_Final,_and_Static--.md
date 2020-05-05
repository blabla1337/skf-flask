## Description:

The program declares an array public, final, and static, which is not sufficient to prevent the array's contents from being modified.

Because arrays are mutable objects, the final constraint requires that the array object itself be assigned only once, but makes no guarantees about the values of the array elements. Since the array is public, a malicious program can change the values stored in the array. As such, in most cases an array declared public, final and static is a bug.

## Mitigation:


PHASE:Implementation:
In most situations the array should be made private.

