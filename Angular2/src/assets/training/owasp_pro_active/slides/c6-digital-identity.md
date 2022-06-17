# C6: Implement Digital Identity

## Description
Digital Identity is the unique representation of a user (or other subject) as they engage in an online transaction. Authentication is the process of verifying that an individual or entity is who they claim to be. Session management is a process by which a server maintains the state of the users authentication so that the user may continue to use the system without re-authenticating. The [NIST Special Publication 800-63B: Digital Identity Guidelines (Authentication and Lifecycle Management](https://pages.nist.gov/800-63-3/sp800-63b.html) provides solid guidance on implementing digital identity, authentication and session management controls.

Below are some recommendations for secure implementation.

## Authentication Levels
NIST 800-63b describes three levels of a authentication assurance called a authentication assurance level (AAL). AAL level 1 is reserved for lower-risk applications that do not contain PII or other private data. At AAL level 1 only single-factor authentication is required, typically through the use of a password. 

### Level 1 : Passwords
Passwords are really really important. We need policy, we need to store them securely, we need to sometimes allow users to reset them.

#### Password Requirements
Passwords should comply with the following requirements at the very least:

* be at least 8 characters in length if multi-factor authentication (MFA) and other controls are also used. If MFA is not possible, this should be increased to at least 10 characters
* all printing ASCII characters as well as the space character should be acceptable in memorized secrets
* encourage the use of long passwords and passphrases
* remove complexity requirements as these have been found to be of limited effectiveness. Instead, the adoption of MFA or longer password lengths is recommended
* ensure that passwords used are not commonly used passwords that have been already been leaked in a previous compromise.  You may choose to block the top 1000 or 10000 most common passwords which meet the above length requirements and are found in compromised password lists. The following link contains the most commonly found passwords: https://github.com/danielmiessler/SecLists/tree/master/Passwords.

#### Implement Secure Password Recovery Mechanism
It is common for an application to have a mechanism for a user to gain access to their account in the event they forget their password. A good design workflow for a password recovery feature will use multi-factor authentication elements. For example, it may ask a security question - something they know, and then send a generated token to a device - something they own.

Please see the [Forgot_Password_Cheat_Sheet](https://www.owasp.org/index.php/Forgot_Password_Cheat_Sheet) and [Choosing_and_Using_Security_Questions_Cheat_Sheet](https://www.owasp.org/index.php/Choosing_and_Using_Security_Questions_Cheat_Sheet) for further details.

#### Implement Secure Password Storage
In order to provide strong authentication controls, an application must securely store user credentials. Furthermore, cryptographic controls should be in place such that if a credential (e.g., a password) is compromised, the attacker does not immediately have access to this information.

**PHP Example for Password Storage**

Below is an example for secure password hashing in PHP using `password_hash()` function (available since 5.5.0) which defaults to using the bcrypt algorithm. The example uses a work factor of 15.

    <?php
     $cost = 15;
     $password_hash = password_hash("secret_password", PASSWORD_DEFAULT,["cost" => $cost]); 
    ?>

Please see the [OWASP Password Storage Cheat Sheet](https://www.owasp.org/index.php/Password_Storage_Cheat_Sheet) for further details.

### Level 2 : Multi-Factor Authentication
NIST 800-63b AAL level 2 is reserved for higher-risk applications that contain "self-asserted PII or other personal information made available online." At AAL level 2 multi-factor authentication is required including OTP or other forms of multi-factor implementation.

Multi-factor authentication (MFA) ensures that users are who they claim to be by requiring them to identify themselves with a combination of:
* Something you know – password or PIN
* Something you own – token or phone
* Something you are – biometrics, such as a fingerprint

Using passwords as a sole factor provides weak security. Multi-factor solutions provide a more robust solution by requiring an attacker to acquire more than one element to authenticate with the service.

It is worth noting that biometrics, when employed as a single factor of authentication, are not considered acceptable secrets for digital authentication. They can be obtained online or by taking a picture of someone with a camera phone (e.g., facial images) with or without their knowledge, lifted from objects someone touches (e.g., latent fingerprints), or captured with high resolution images (e.g., iris patterns). Biometrics must be used only as part of multi-factor authentication with a physical authenticator (something you own). For example, accessing a multi-factor one-time password (OTP) device that will generate a one-time password that the user manually enters for the verifier.

### Level 3 : Cryptographic Based Authentication
NIST 800-63b Authentication Assurance Level 3 (AAL3) is required when the impact of compromised systems could lead to personal harm, significant financial loss, harm the public interest or involve civil or criminal violations. AAL3 requires authentication that is "based on proof of possession of a key through a cryptographic protocol." This type of authentication is used to achieve the strongest level of authentication assurance. This is typically done though hardware cryptographic modules.

#### Session Management
Once the initial successful user authentication has taken place, an application may choose to track and maintain this authentication state for a limited amount of time. This will allow the user to continue using the application without having to keep re-authentication with each request. Tracking of this user state is called Session Management. 

#### Session Generation and Expiration
User state is tracked in a session. This session is typically stored on the server for traditional web based session management. A session identifier is then given to the user so the user can identify which server-side session contains the correct user data. The client only needs to maintain this session identifier, which also keeps sensitive server-side session data off of the client.

Here are a few controls to consider when building or implementing session management solutions:

* Ensure that the session id is long, unique and random.
* The application should generate a new session or at least rotate the session id during authentication and re-authentication.
* The application should implement an idle timeout after a period of inactivity and an absolute maximum lifetime for each session, after which users must re-authenticate. The length of the timeouts should be inversely proportional with the value of the data protected.

Please see the [Session Management Cheat Sheet](https://www.owasp.org/index.php/Session_Management_Cheat_Sheet) further details. ASVS Section 3 covers additional session management requirements.

#### Browser Cookies
Browser cookies are a common method for web application to store session identifiers for web applications implementing standard session management techniques. Here are some defenses to consider when using browser cookies.

* When browser cookies are used as the mechanism for tracking the session of an authenticated user,  these should be accessible to a minimum set of domains and paths and should be tagged to expire at, or soon after, the session's validity period.
* The 'secure' flag should be set to ensure the transfer is done via secure channel only (TLS).
* HttpOnly flag should be set to prevent the cookie from  being accessed via JavaScript.
* Adding "[samesite](https://www.owasp.org/index.php/SameSite)" attributes to cookies prevents some [modern browsers](https://caniuse.com/#search=samesite) from sending cookies with cross-site requests and provides protection against cross-site request forgery and information leakage attacks.

#### Tokens
Server-side sessions can be limiting for some forms of authentication. "Stateless services" allow for client side management of session data for performance purposes so they server has less of a burden to store and verify user session. These "stateless" applications generate a short-lived access token which can be used to authenticate a client request without sending the user's credentials after the initial authentication.

#### JWT (JSON Web Tokens)
JSON Web Token (JWT) is an open standard ([RFC 7519](https://tools.ietf.org/html/rfc7519) ) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. This information can be verified and trusted because it is digitally signed. A JWT token is created during authentication and is verified by the server (or servers) before any processing.

However, JWT's are often not saved by the server after initial creation. JWT's are typically created and then handed to a client without being saved by the server in any way. The integrity of the token is maintained through the use of digital signatures so a server can later verify that the JWT is still valid and was not tampered with since its creation.

This approach is both stateless and portable in the way that client and server technologies can be different yet still interact.

**Caution** 

Digital identity, authentication and session management are very big topics. We're scratching the surface of the topic of Digital Identity here. Ensure that your most capable engineering talent is responsible for maintaining the complexity involved with most Identity solutions.

## Vulnerabilities Prevented
* [OWASP Top 10 2017 A2- Broken Authentication and Session Management](https://www.owasp.org/index.php/Top_10-2017_A2-Broken_Authentication)
* [OWASP Mobile Top 10 2014-M5- Poor Authorization and Authentication](https://www.owasp.org/index.php/Mobile_Top_10_2014-M5)

## References
* [OWASP Cheat Sheet: Authentication](https://www.owasp.org/index.php/Authentication_Cheat_Sheet)
* [OWASP Cheat Sheet: Password Storage](https://www.owasp.org/index.php/Password_Storage_Cheat_Sheet)
* [OWASP Cheat Sheet: Forgot Password](https://www.owasp.org/index.php/Password_Storage_Cheat_Sheet)
* [OWASP Cheat Sheet: Choosing and Using Security Questions](https://www.owasp.org/index.php/Choosing_and_Using_Security_Questions_Cheat_Sheet)
* [OWASP Cheat Sheet: Session Management](https://www.owasp.org/index.php/Session_Management_Cheat_Sheet)
* [OWASP Cheat Sheet: IOS Developer](https://www.owasp.org/index.php/IOS_Developer_Cheat_Sheet)
* [OWASP Testing Guide: Testing for Authentication](https://www.owasp.org/index.php/Testing_for_authentication)
* [NIST Special Publication 800-63 Revision 3 - Digital Identity Guidelines](https://pages.nist.gov/800-63-3/sp800-63-3.html)

## Tools
* Daniel Miessler: [Most commonly found passwords](https://github.com/danielmiessler/SecLists/tree/master/Passwords)
