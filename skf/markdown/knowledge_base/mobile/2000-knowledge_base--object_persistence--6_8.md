## Description:

Object Persistence

MSTG-PLATFORM-8: Object deserialization, if any, is implemented using safe serialization APIs.

Serialization is the process of turning some object into a data format that can be restored later. People often serialize objects in order to save them to storage, or to send as part of communications.

Deserialization is the reverse of that process, taking data structured from some format, and rebuilding it into an object. Today, the most popular data format for serializing data is JSON. Before that, it was XML.

However, many programming languages offer a native capability for serializing objects. These native formats usually offer more features than JSON or XML, including customizability of the serialization process.

Unfortunately, the features of these native deserialization mechanisms can be repurposed for malicious effect when operating on untrusted data. Attacks against deserializers have been found to allow denial-of-service, access control, and remote code execution (RCE) attacks.

There are several ways to persist an object on Android:

	- Object Serialization
	- JSON
	- XML
	- ORM
	- Parcelable
	- Protocol Buffers

There are several ways to persist an object on iOS:

	- Object Encoding:
	- Object Archiving with NSKeyedArchiver:
	- Codable
	- JSON and Codable
	- Property Lists and Codable
	- XML
	- Object-Relational Mapping (CoreData and Realm)
	- Protocol Buffers


## Mitigation:

There are a few generic remediation steps that you can always take:

	1. Make sure that sensitive data has been encrypted and HMACed/signed after serialization/persistence. Evaluate the signature or HMAC before you use the data. See the chapter "[Android Cryptographic APIs](0x05e-Testing-Cryptography.md)" for more details.
	2. Make sure that the keys used in step 1 can't be extracted easily. The user and/or application instance should be properly authenticated/authorized to obtain the keys. See the chapter "[Data Storage on Android](0x05d-Testing-Data-Storage.md)" for more details.
	3. Make sure that the data within the de-serialized object is carefully validated before it is actively used (e.g., no exploit of business/application logic).
