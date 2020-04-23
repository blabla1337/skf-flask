## Description:

The program defines a signal handler that calls a non-reentrant function.

Non-reentrant functions are functions that cannot safely be called, interrupted, and then recalled before the first call has finished without resulting in memory corruption. This can lead to an unexpected system state and unpredictable results with a variety of potential consequences depending on context, including denial of service and code execution. Many functions are not reentrant, but some of them can result in the corruption of memory if they are used in a signal handler. The function call syslog() is an example of this. In order to perform its functionality, it allocates a small amount of memory as scratch space. If syslog() is suspended by a signal call and the signal handler calls syslog(), the memory used by both of these functions enters an undefined, and possibly, exploitable state. Implementations of malloc() and free() manage metadata in global structures in order to track which memory is allocated versus which memory is available, but they are non-reentrant. Simultaneous calls to these functions can cause corruption of the metadata.

## Mitigation:


PHASE:Requirements:
Require languages or libraries that provide reentrant functionality, or otherwise make it easier to avoid this weakness.

PHASE:Architecture and Design:
Design signal handlers to only set flags rather than perform complex functionality.

PHASE:Implementation:
Ensure that non-reentrant functions are not found in signal handlers.

PHASE:Implementation:
Use sanity checks to reduce the timing window for exploitation of race conditions. This is only a partial solution, since many attacks might fail, but other attacks still might work within the narrower window, even accidentally.:EFFECTIVENESS:Defense in Depth

