
XML injection
-------

**Description:**

XML Injection is an attack technique used to manipulate or compromise the logic of an XML
application or service. The injection of unintended XML content and/or structures into
an XML message can alter the intend logic of the application. Further, XML injection
can cause the insertion of malicious content into the resulting message/document.


**Solution:**

In addition to the existing input validation, define a positive approach which
escapes/encodes characters that can be interpreted as xml. At a minimum this includes
the following: < > / " '

	