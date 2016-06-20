
External DTD parsing
-------

**Description:**

Processing of an external entity containing tainted data may lead to disclosure of
confidential information and other system impacts.
The XML 1.0 standard defines the structure of an XML document.
The standard defines a concept called an entity, which is a storage unit of some type. 
There exists a specific type of entity, an external general parsed entity often shortened
to an external entity, that can access local or remote content via a declared system
identifier. The system identifier is assumed to be a URI that can be dereferenced
(accessed) by the XML processor when processing the entity. 

The XML processor then
replaces occurrences of the named external entity with the contents dereferenced by the
system identifier. If the system identifier contains tainted data and the XML processor
dereferences this tainted data, the XML processor may disclose confidential information
normally not accessible by the application. Attacks can include disclosing local files,
which may contain sensitive data such as passwords or private user data, 
using file: schemes or relative paths in the system identifier. 

Since the attack occurs relative to the application processing the XML document, 
an attacker may use this trusted application to pivot to other internal systems, 
possibly disclosing other internal content
via http(s) requests. In some situations, an XML processor library that is vulnerable
to client-side memory corruption issues may be exploited by dereferencing a malicious URI, 
possibly allowing arbitrary code execution under the application account. Other attacks 
can access local resources that may not stop returning data, possibly impacting application 
availability if too many threads or processes are not released. 


**Solution:**

Disable the XML DTD parsing. This can be set when initiating the XML parser.

	