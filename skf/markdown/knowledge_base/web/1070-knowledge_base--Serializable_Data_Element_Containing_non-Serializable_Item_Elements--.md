## Description:

The software contains a serializable, storable data element such as a field or member, but the data element contains member elements that are not serializable.

This issue can prevent the software from running reliably. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability. As examples, the serializable nature of a data element comes from a serializable SerializableAttribute attribute in .NET and the inheritance from the java.io.Serializable interface in Java.

## Mitigation:
