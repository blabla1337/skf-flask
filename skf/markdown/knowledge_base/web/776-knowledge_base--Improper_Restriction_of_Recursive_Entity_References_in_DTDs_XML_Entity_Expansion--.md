##Description:

The software uses XML documents and allows their structure to be defined with a Document Type Definition (DTD), but it does not properly control the number of recursive definitions of entities.

If the DTD contains a large number of nested or recursive entities, this can lead to explosive growth of data when parsed, causing a denial of service.

##Mitigation:


PHASE:Operation:
If possible, prohibit the use of DTDs or use an XML parser that limits the expansion of recursive DTD entities.

PHASE:Implementation:
Before parsing XML files with associated DTDs, scan for recursive entity declarations and do not continue parsing potentially explosive content.

