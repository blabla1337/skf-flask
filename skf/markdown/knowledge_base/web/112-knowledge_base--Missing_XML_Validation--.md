##Description:

The software accepts XML from an untrusted source but does not validate the XML against the proper schema.

Most successful attacks begin with a violation of the programmer's assumptions. By accepting an XML document without validating it against a DTD or XML schema, the programmer leaves a door open for attackers to provide unexpected, unreasonable, or malicious input.

##Mitigation:


PHASE:Architecture and Design:STRATEGY:Input Validation:
Always validate XML input against a known XML Schema or DTD. It is not possible for an XML parser to validate all aspects of a document's content because a parser cannot understand the complete semantics of the data. However, a parser can do a complete and thorough job of checking the document's structure and therefore guarantee to the code that processes the document that the content is well-formed.

