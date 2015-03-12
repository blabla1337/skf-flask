
Character encoding
-------

**Description:**

Character encoding is the process of mapping characters, numbers and other symbols to a 
standard format. Typically, this is done to create a message ready for transmission 
between sender and receiver. It is, in simple terms, the conversion of characters 
(belonging to different languages like English, Chinese, Greek or any other known language) 
into bytes. An example of a widely used character encoding scheme is the American 
Standard Code for Information Interchange (ASCII) that initially used 7-bit codes. 
More recent examples of encoding schemes would be the Unicode UTF-8 and UTF-16 computing 
industry standards. In the space of application security and due to the plethora of 
encoding schemes available, character encoding has a popular misuse. It is being used for 
encoding malicious injection strings in a way that obfuscates them. This can lead to the 
bypass of input validation filters, or take advantage of particular ways in which browsers 
render encoded text.


**Solution:**

These three ways of providing the character encoding of a document are not equivalent. 
When trying to figure out the character encoding of a resource, user agents will try, in 
this order: The HTTP Content-Type header sent by the server, the XML declaration 
(only for XHTML documents) or the HTML/XHTML meta element.

	