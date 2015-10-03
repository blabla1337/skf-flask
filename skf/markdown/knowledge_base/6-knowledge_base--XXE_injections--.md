
XXE injections
-------

**Description:**

Processing of an Xml eXternal Entity containing tainted data may lead to disclosure of 
confidential information and other system impacts. 
The XML 1.0 standard defines the structure of an XML document. 
The standard defines a concept called an entity, which is a storage unit of some type.

There exists a specific type of entity, an external general parsed entity often shortened
to an external entity, that can access local or remote content via a declared system 
identifier and the XML processor may disclose confidential information normally not 
accessible by the application. Attacks can include disclosing local files, which may 
contain sensitive data such as passwords or private 


**Solution:**

Disable the possibility to fetch resources from an external source.
This is normally done in the config of the used XML parser.

	