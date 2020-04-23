## Description:

The application deserializes untrusted data without sufficiently verifying that the resulting data will be valid.

It is often convenient to serialize objects for communication or to save them for later use. However, deserialized data or code can often be modified without using the provided accessor functions if it does not use cryptography to protect itself. Furthermore, any cryptography would still be client-side security -- which is a dangerous security assumption. Data that is untrusted can not be trusted to be well-formed. When developers place no restrictions on gadget chains, or series of instances and method invocations that can self-execute during the deserialization process (i.e., before the object is returned to the caller), it is sometimes possible for attackers to leverage them to perform unauthorized actions, like generating a shell.

## Mitigation:


PHASE:Architecture and Design Implementation:
If available, use the signing/sealing features of the programming language to assure that deserialized data has not been tainted. For example, a hash-based message authentication code (HMAC) could be used to ensure that data has not been modified.

PHASE:Implementation:
When deserializing data, populate a new object rather than just deserializing. The result is that the data flows through safe input validation and that the functions are safe.

PHASE:Implementation:
Explicitly define a final object() to prevent deserialization.

PHASE:Architecture and Design Implementation:
Make fields transient to protect them from deserialization. An attempt to serialize and then deserialize a class containing transient fields will result in NULLs where the transient data should be. This is an excellent way to prevent time, environment-based, or sensitive variables from being carried over and used improperly.

PHASE:Implementation:
Avoid having unnecessary types or gadgets available that can be leveraged for malicious ends. This limits the potential for unintended or unauthorized types and gadgets to be leveraged by the attacker. Whitelist acceptable classes. Note: new gadgets are constantly being discovered, so this alone is not a sufficient mitigation.

