Client side input validation
-------

**Description:**

Because web applications become more advanced, in the sepperation of the pure
front-end part (client-side code) and the back-end (server-side code). This also 
results in more XSS vulnerabilities in the JavaScript on the client-side rather than 
by the server. The client-side code might still unsafely include user input in a DOM update 
after the page has loaded. If this happens, the client-side code has enabled an XSS attack 
through no fault of the server-side code.

**Solution:**

First there must be a client side input validation method as you would apply to the server
side. This means you should also apply input rejection as wel as typecasting and such.
This is to prevent users from being attacked by XSS attacks which are undetectable by
the server.

Recommended knowledge base items:
- Positive validation method
- Single input validation controls
- Input rejection
- Input validation




   
