
Client side Caching and HTML5 Caching
-------

**Description:**

Developers creating HTML5 applications can create fully offline-aware applications using 
the HTML5 ApplicationCache interface. The Application Cache uses a cache manifest file to 
specify which files in an HTML5 application can be used offline, and which files require a 
network connection.


**Solution:**

Never store sensitive information in a client side cache since this can be easily 
compromised by attackers. The same principle does also apply to autocomplete functions.

	