
# Question

Which of the following methods are supported by HTTP (RFC 7231, RFC 5789)? Can choose multiple answers.

* ( ) GET
* ( ) POST
* ( ) HEAD
* ( ) PUT
* ( ) UNLOCK
* ( ) DELETE
* ( ) CONNECT
* ( ) OPTIONS
* ( ) PROPFIND
* ( ) MOVE
* ( ) TRACE
* ( ) PATCH
* ( ) CONNECT
* ( ) None of the above 

-----SPLIT-----

# Answer

* (x) GET
* (x) POST
* (x) HEAD
* (x) PUT
* ( ) UNLOCK
* (x) DELETE
* (x) CONNECT
* (x) OPTIONS
* ( ) PROPFIND
* ( ) MOVE
* (x) TRACE
* (x) PATCH
* (x) CONNECT
* ( ) None of the above 

Explanation: HTTP (RFC 7231, RFC 5789) does not include UNLOCK, PROPFIND, MOVE methods. They are defined in RFC2518, Web-based distributed authoring and versioning (WebDAV) is a set of extensions to the HTTP protocol.

-----SPLIT-----

# Question

Decide if the given statmen is true or false.

"Making an HTTP OPTION request to a web server returns a list of available supported HTTP methods which are reliable and absolutely correct."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* ( ) True
* (x) False


Explanation: Some servers may not respond to OPTIONS requests, or may return inaccurate information. An more reliable way to test for supported methods is to simply make a request with that method type, and examine the server response. If the method is not permitted, the server should return a 405 Method Not Allowed status.

-----SPLIT-----

# Question

Decide if the given statmen is true or false.

"Some legacy web servers allowed the use of the HTTP PUT method to create files on the server."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* (x) True
* ( ) False

-----SPLIT-----

# Question

Decide if the given statmen is true or false.

"The TRACE method (or Microsoft's equivalent TRACK method) causes the server to echo back the contents of the request."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* (x) True
* ( ) False

-----SPLIT-----

# Question

Decide if the given statmen is true or false.

"Cross-Site Tracing (XST) can be used to access cookies that had the HttpOnly flag set."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* (x) True
* ( ) False

-----SPLIT-----

# Question

Decide if the given statmen is true or false.

"JSON PATCH method overwrites the entire object by requiring all the proper fields in JSON body."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* ( ) True
* (x) False

Explanation: JSON PATCH method allow to update some part of objects. This is in contrast to the PUT method, which would overwrite the entire object.

-----SPLIT-----

# Question

Complete the following sentence with suitable term.

'The purpose of using ............., by adding X-HTTP-Method, X-HTTP-Method-Override or X-Method-Override headers in a request header, is is to circumvent a middleware application (such as a proxy or web application firewall) which blocks specific methods.'

* ( ) HTTP Overloading
* ( ) HTTP Overriding
* ( ) HTTP Inheritance
* ( ) None of the above 

-----SPLIT-----

# Answer

* ( ) HTTP Overloading
* (x) HTTP Overriding
* ( ) HTTP Inheritance
* ( ) None of the above 

