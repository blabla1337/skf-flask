## Description:

The software contains a serializable data element that does not have an associated serialization method.

This issue can prevent the software from running reliably, e.g. by triggering an exception. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability. As examples, the serializable nature of a data element comes from a serializable SerializableAttribute attribute in .NET and the inheritance from the java.io.Serializable interface in Java.

## Mitigation:
