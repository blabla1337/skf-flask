## Input Validation: Beyond Numbers and Text

### Insecure Deserialization

Don’t just blindly accept more complex data formats. Instead, ensure that accepting that input from an untrusted source will not cause a security problem.

A dangerous problem is insecure deserialization. **Deserialization** is the process of converting some sequence (of bytes or characters) into some internal format; that process may create a number of objects. Deserialization can happen when reading data from a network or from storage, because in both cases there is a need to turn a sequence of bytes or characters into an internal format. Unfortunately, deserialization can result in serious problems, because if the source is untrusted, then the attacker may provide a manipulated sequence:

1. The data might be converted into an unexpected value that you should not trust. For example, it might be a structured cookie value that originally said **admin=n**, but the attacker may change the value to **admin=y**. If the program blindly accepted this data, the attacker might suddenly become an administrator!

2. Deserializing the data might cause code execution, e.g., it might create classes or instances and/or call attacker-selected methods with attacker-provided arguments. This is especially a problem for formats designed for arbitrary object persistence. An example of this is the Python pickle format, which automatically executes code in certain cases when deserializing data.

** The safest solution is to not accept serialized objects from untrusted sources.**

If you must accept serialized objects from untrusted sources, you can use serialization formats that do not support code execution. For example, use serialization formats that only allow primitive data types. This counters the second problem - code execution - but by itself, it does not solve the first problem - unexpected values. So, if after choosing an approach to prevent code execution, validate the input you have received using the approaches we have already discussed.

In some cases, you can prevent deserialization attacks with authentication checks. Basically, turn untrusted data into trusted data! To do this, before you deserialize the data, run an authentication check to ensure that the data is from a trusted source. A common way to do this is by checking a digital signature, message authentication code (MAC), authenticated encryption, or similar measure. This approach is especially common in web applications; often, a web server will send data to a client, so that the client can later send it back (e.g., as a cookie). This approach is fine as long as the web server verifies its integrity (to prevent attacker creation or tampering) *before* it is deserialized.

Some people recommend enforcing string type constraints (e.g., only allowing specific classes to be deserialized). Unfortunately, many bypasses to this technique have been found over the years. It is a good idea as a *hardening* technique (or simply as a way to detect bugs early). However, in many systems, this is probably too dangerous to recommend as an adequate defense by itself.

Insecure deserialization is such a common mistake in web applications that it is 2017 OWASP Top 10 #8 and 2019 CWE Top 25 #23. It is [CWE-502](https://cwe.mitre.org/data/definitions/502.html), *Deserialization of Untrusted Data*. Attackers may find such vulnerabilities harder to exploit, but once the vulnerability is found it can result in immediate compromise of an entire system, because it may provide complete control of the system to the attacker.