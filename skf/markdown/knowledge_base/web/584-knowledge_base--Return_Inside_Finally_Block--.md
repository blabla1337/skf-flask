## Description:

The code has a return statement inside a finally block, which will cause any thrown exception in the try block to be discarded.



## Mitigation:


PHASE:Implementation:
Do not use a return statement inside the finally block. The finally block should have cleanup code.

