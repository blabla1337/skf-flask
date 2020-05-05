## Description:

The program calls a thread's run() method instead of calling start(), which causes the code to run in the thread of the caller instead of the callee.

In most cases a direct call to a Thread object's run() method is a bug. The programmer intended to begin a new thread of control, but accidentally called run() instead of start(), so the run() method will execute in the caller's thread of control.

## Mitigation:


PHASE:Implementation:
Use the start() method instead of the run() method.

