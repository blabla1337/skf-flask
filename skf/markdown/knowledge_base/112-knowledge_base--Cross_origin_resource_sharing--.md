
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
that are supported by all major browsers:

- Origin 
- Access-Control-Request-Method
- Access-Control-Request-Headers 
- Access-Control-Allow-Origin
- Access-Control-Allow-Credentials 
- Access-Control-Allow-Methods
- Access-Control-Allow-Headers

Things you must consider when using CORS

1. Validate URLs passed to XMLHttpRequest.open. Current browsers allow these URLs to be 
   cross domain; this behavior can lead to code injection by a remote attacker. Pay extra 
   attention to absolute URLs.

2. Ensure that URLs responding with Access-Control-Allow-Origin: * do not include any 
   sensitive content or information that might aid attacker in further attacks. 
   Use the Access-Control-Allow-Origin header only on chosen URLs that need to be 
   accessed cross-domain. Don't use the header for the whole domain.

3. Allow only selected, trusted domains in the Access-Control-Allow-Origin header. 
   Prefer whitelisting domains over blacklisting or allowing any domain 
   (do not use * wildcard nor blindly return the Origin header content without any checks)

4. Keep in mind that CORS does not prevent the requested data from going to an
   unauthenticated location. It's still important for the server to perform usual 
   CSRF prevention.
  
5. While the RFC recommends a pre-flight request with the OPTIONS verb, current 
   implementations might not perform this request, so it's important that "ordinary" 
   (GET and POST) requests perform any access control necessary.

6. Discard requests received over plain HTTP with HTTPS origins to prevent mixed 
   content bugs.

7. Don't rely only on the Origin header for Access Control checks. Browser always sends 
   this header in CORS requests, but may be spoofed outside the browser. 
   Application-level protocols should be used to protect sensitive data.
