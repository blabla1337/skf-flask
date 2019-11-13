## Description:

JSON Web Token (JWT) is an open standard (RFC 7519) that defines a compact and self-contained way 
for securely transmitting information between parties as a JSON object. This information can be verified and 
trusted because it is digitally signed. JWTs can be signed using a secret (with the HMAC algorithm) or a public/private key pair using RSA.

JSON Web Token is used to carry information related to the identity and characteristics (claims) of a client. This "container" is signed by the server in order to avoid that a client tamper it in order to change, for example, the identity or any characteristics (example: change the role from simple user to admin or change the client login).

This token is created during authentication (is provided in case of successful authentication) and is verified by the server before any processing. It is used by an application to allow a client to present a token representing his "identity card" (container with all information about him) to server and allow the server to verify the validity and integrity of the token in a secure way, all of this in a stateless and portable approach (portable in the way that client and server technologies can be different including also the transport channel even if HTTP is the most often used).

## Solution:

For more information about all the different implementation flaws for JWT please refer to:

https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/JSON_Web_Token_Cheat_Sheet_for_Java.md
