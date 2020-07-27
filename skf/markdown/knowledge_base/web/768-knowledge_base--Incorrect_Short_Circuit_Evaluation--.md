##Description:

The software contains a conditional statement with multiple logical expressions in which one of the non-leading expressions may produce side effects. This may lead to an unexpected state in the program after the execution of the conditional, because short-circuiting logic may prevent the side effects from occurring.

Usage of short circuit evaluation, though well-defined in the C standard, may alter control flow in a way that introduces logic errors that are difficult to detect, possibly causing errors later during the software's execution. If an attacker can discover such an inconsistency, it may be exploitable to gain arbitrary control over a system. If the first condition of an or statement is assumed to be true under normal circumstances, or if the first condition of an and statement is assumed to be false, then any subsequent conditional may contain its own logic errors that are not detected during code review or testing. Finally, the usage of short circuit evaluation may decrease the maintainability of the code.

##Mitigation:


PHASE:Implementation:
Minimizing the number of statements in a conditional that produce side effects will help to prevent the likelihood of short circuit evaluation to alter control flow in an unexpected way.

