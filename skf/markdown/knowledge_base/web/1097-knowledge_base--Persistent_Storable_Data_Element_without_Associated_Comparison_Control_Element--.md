##Description:

The software uses a storable data element that does not have all of the associated functions or methods that are necessary to support comparison.

For example, with Java, a class that is made persistent requires both hashCode() and equals() methods to be defined. This issue can prevent the software from running reliably, due to incorrect or unexpected comparison results. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability.

##Mitigation:
