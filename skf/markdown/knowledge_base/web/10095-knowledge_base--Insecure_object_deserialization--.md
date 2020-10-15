##Description:

Serialization is the process of turning some object into a data format that can be restored later. 
People often serialize objects in order to save them to storage, or to send as part of communications.

Deserialization is the reverse of that process, taking data structured from some format, and rebuilding it
into an object. Today, the most popular data format for serializing data is JSON. Before that, it was XML.

However, many programming languages offer a native capability for serializing objects. These native formats
usually offer more features than JSON or XML, including customizability of the serialization process.

Unfortunately, the features of these native deserialization mechanisms can be repurposed for malicious
effect when operating on untrusted data. Attacks against deserializers have been found to allow denial-of-service,
access control, and remote code execution (RCE) attacks.


##Mitigation:

Verify that serialized objects use integrity checks or are encrypted to prevent hostile object creation or data tampering.

A great reduction of risk is achieved by avoiding native (de)serialization formats. By switching to a 
pure data format like JSON or XML, you lessen the chance of custom deserialization logic being repurposed 
towards malicious ends.

Many applications rely on a data-transfer object pattern that involves creating a separate domain of 
objects for the explicit purpose data transfer. Of course, it's still possible that the application 
will make security mistakes after a pure data object is parsed.

If the application knows before deserialization which messages will need to be processed, 
they could sign them as part of the serialization process. The application could then to 
choose not to deserialize any message which didn't have an authenticated signature.
