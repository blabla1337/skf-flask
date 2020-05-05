## Description:

The code contains a switch statement in which the switched variable can be modified while the switch is still executing, resulting in unexpected behavior.

This issue is particularly important in the case of switch statements that involve fall-through style case statements - i.e., those which do not end with break. If the variable being tested by the switch changes in the course of execution, this could change the intended logic of the switch so much that it places the process in a contradictory state and in some cases could even result in memory corruption.

## Mitigation:


PHASE:Implementation:
Variables that may be subject to race conditions should be locked before the switch statement starts and only unlocked after the statement ends.

