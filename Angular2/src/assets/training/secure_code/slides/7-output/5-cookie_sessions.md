### Cookies & Login Sessions

[Web application]

An important mechanism in the HTTP protocol is support for *cookies*. Cookies are small chunks of data sent from a web server to a web browser. From then on, when the web browser contacts that web server, the web browser will send that cookie value back to the server it came from, subject to certain restrictions.

#### Cookie Attributes

Web servers can also set some attributes on the cookies they send. For example:

* Expiration time: If no expiration time is set, the cookie expires when the browser exits (such cookies are called *session cookies*). Otherwise, the browser may store the cookie permanently until the time expires (such cookies are called *permanent cookies* - a user *can* delete these cookies, but few do).

* **Secure** flag: If set, the cookie will only be sent to HTTPS servers, and not to HTTP. You should set this whenever practical.

* **HttpOnly** flag: The cookie is not visible to JavaScript programs. You should set this whenever practical.

* **SameSite**: This has three main values - **None**, **Lax**, and **Strict**. “**None**” means that cookies are always sent to the matching web server. “**Lax**” means that cookies are sent if they are a **GET** (click) on a third-party website, and otherwise cookies are only sent if the request comes from the same site. “**Strict**” means that cookies are only sent in a first-party context; any request from another website will *not* cause the cookie to be sent. Historically, the web browser default was effectively **None**, but modern web browsers now act with **Lax** as the default because this counters certain attacks. We will discuss this later, but you should set this to at least **Lax** wherever practical.

#### Cookies in Context

Cookies are not, by themselves, necessarily malicious. However, cookies can reveal who the requester is in some cases, making them a potential privacy issue. This is especially true for cookies that have **SameSite=None**. If someone sets up requests for this kind of cookie on many websites (e.g., by embedding third-party images), the cookie can be used to track that user’s actions across many sites. A cookie intended to track users across websites is called a *tracking cookie*. Tracking cookies can be even worse if they have a long expiration time, because such cookies persist after the browser exits. Tracking cookies have attracted the concerns of many nations because of their detrimental effect on user privacy. As a result, various laws have passed involving cookies and consent. However, implementing tracking cookies is not the only way to use cookies; cookies can also improve security.

Cookies are important in part because they are often used to implement login sessions on the world wide web (WWW). A login session is simply a period of activity between when a user logs in and logs out. The original WWW protocol did not have a way to implement login sessions, and cookies provide a simple mechanism to support login sessions.

#### Cookies and Login Sessions

On the web, a common way to implement a login session is to have a login form. If the login is successful, the web server sends a “**session id**” within a cookie value. The session id is simply a large random number that cannot be guessed by anyone else. From then on, the web browser then sends this cookie (with the session id) whenever it contacts that web server. The web server can check this session id to see who is making the request… and if that session id is valid, the web server looks up the user id for that session and allows the user to whatever the user is authorized to do. Including a session id in a cookie is **not** the only way to use cookies to support login, but it is a common approach.

Normally, when developing web applications, you will use a framework or library that (mostly) handles login sessions for you. This is fine, just check to ensure that it is secure. Here we will cover some key features to look for. In some cases, your framework won’t do it by itself, but you can take some additional steps to make them happen.

First, if your framework uses session ids in cookies (a common approach), it is critical that the implementation does not allow attackers to guess or discover the session ids. If an attacker can get the session id, the attacker can act with the same privileges as the logged-in user! In this common case, check for these key factors at least:

1. The session identifier must have at least 128 bits of random data.

2. The session id must be created using a *cryptographically secure* pseudo-random number generator (CSPRNG). Anything guessable (like *“add one to the last session id”* or *“ordinary call to random()”)* is not acceptable. We will discuss this in more detail later.

3. Encrypt session ids between the web server and web browser. The usual solution is to set the cookie’s **Secure** flag and always communicate using HTTPS (TLS).

Second, set the attributes of cookies that contain session ids to be secure:

1. As noted earlier, where practical set cookies for login session handling with the **HttpOnly** flag. That way, JavaScript programs won’t have direct access to it. This is another example of least privilege; if a privilege is not needed, don’t provide the access.

2. Similarly, consider using session cookies (cookies with no expiration time) for cookies that store information on login sessions. You don’t have to do this; you can use permanent cookies to store session information. But if you use permanent cookies, consider limiting the time to at most a few days. Permanent cookies are stored in permanent storage, and an attacker might be able to gain access to that stored information.

Third, make sure that you have login and logout functions, and that they actually work correctly!

Whenever a user successfully logs in, make sure that the user *always* gets a *new* session id (this is typically returned in a cookie). In particular, the receiving side of a login must *never* reuse session values. A new login means a new session is being requested (even if there is already a current session), so make sure a new session is created and used for that request! If your program fails to create a new session for a new login, it may be vulnerable to a *session fixation attack*.

Session fixation is such a common cause of security vulnerabilities that it is 2019 CWE Top 25 #37. It is [CWE-384](https://cwe.mitre.org/data/definitions/384.html).

Similarly, make *sure* that you provide users a “log off” (“sign off”) action that *actually works*. If you use session ids - a common approach - then a log off should invalidate that session. This generally means that you need to remove the record of that session id from the server database that records active session ids (and the user id each session id applies to). You also need to tell the browser to delete the cookie or at least the session id value in that cookie. That way, the user is actually logged out. Users log out to reduce their risks, but this does not work if the application does not actually log them out. A surprisingly large number of major sites have, at one time or another, not logged out users when they requested it.

You should also eventually log out an inactive session automatically. Some easy ways to do that are to not set an expiration date (so the user will log out when they shut down their browser) or set an expiration date for when the user will be logged out. Frameworks will typically let you configure this easily.