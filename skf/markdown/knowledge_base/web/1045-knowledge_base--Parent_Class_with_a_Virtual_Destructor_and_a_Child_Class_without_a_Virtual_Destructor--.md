##Description:

A parent class has a virtual destructor method, but the parent has a child class that does not have a virtual destructor.

This issue can prevent the software from running reliably, since the child might not perform essential destruction operations. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability, such as a memory leak (CWE-401).

##Mitigation:
