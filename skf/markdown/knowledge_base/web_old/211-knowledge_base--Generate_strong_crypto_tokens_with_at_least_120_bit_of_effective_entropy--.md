##Description:

ID values stored on the device such as IMEI and UDID should not be used as authentication 
tokens. These tokens are retrievable by other applications and thus warrant no integrity.
 
Using ID values from the mobile device also implies the use of static API tokens which is 
considered insecure. These tokens cannot for example, expire or be invalidated by the application.
 
Whenever the application uses static tokens such as the ID values and this information is 
leaked by a MiTM attack or leaked in another way then this attacker can now fully compromise 
the user without being able to reject to expire or invalidate the static token EMEI or UDID for example. 

## Solution:

Authentication tokens should always be generic and should be cryptographically random strong 
with at least 120 bit of effective entropy. The best way to implement these tokens is to
go with proven methods that are tested on the effective level of entropy.

For example JSON Web Token (JWT) is an open standard (RFC 7519) that defines a compact and 
self-contained way for securely transmitting information between parties as a JSON object. 
This information can be verified and trusted because it is digitally signed. JWTs can be 
signed using a secret (with the HMAC algorithm) or a public/private key pair using RSA. 
