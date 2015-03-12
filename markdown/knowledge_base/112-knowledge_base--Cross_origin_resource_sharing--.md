
Cross origin resource sharing
-------

**Description:**

Cross Origin Resource Sharing or CORS is a mechanism that enables a web browser to perform 
'cross-domain' requests using the XMLHttpRequest L2 API in a controlled manner. 
In the past, the XMLHttpRequest L1 API only allowed requests to be sent within the same 
origin as it was restricted by the same origin policy.


**Solution:**

Cross-Origin requests have an Origin header, that identifies the domain initiating the 
request and is always sent to the server. CORS defines the protocol to use between a web 
browser and a server to determine whether a cross-origin request is allowed. In order to 
accomplish this goal, there are a few HTTP headers involved in this process, 
that are supported by all major browsers and we will cover below including: 

- Origin 
- Access-Control-Request-Method
- Access-Control-Request-Headers 
- Access-Control-Allow-Origin
- Access-Control-Allow-Credentials 
- Access-Control-Allow-Methods
- Access-Control-Allow-Headers
