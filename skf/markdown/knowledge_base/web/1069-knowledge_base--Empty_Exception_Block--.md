##Description:

An invokable code block contains an exception handling block that does not contain any code, i.e. is empty.

When an exception handling block (such as a Catch and Finally block) is used, but that block is empty, this can prevent the software from running reliably. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability.

##Mitigation:
