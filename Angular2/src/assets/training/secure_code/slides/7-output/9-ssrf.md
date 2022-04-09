### Using Inadequately Checked URLs / Server-Side Request Forgery (SSRF)

A Uniform Resource Locator (URL) is a way to refer to a specific web resource by location. Technically, a URL is a specific type of Uniform Resource Identifier (URI), but for our purposes we will use the terms interchangeably. As specified in [IETF RFC 3986](https://tools.ietf.org/html/rfc3986), a generic URI has this syntax:

**scheme:[//authority]path[?query][#fragment]**

And **authority** has this syntax:

**[userinfo@]host[:port]**

Sometimes untrusted users will give you data that you want to use as a URL (or turn into a URL) to request more information. However, this can be dangerous. If you include a URL in data you present to a user, they might do the equivalent of clicking on it. It turns out that URLs are powerful things, and an attacker might try to exploit any of their capabilities. For example:

* A URL need not use the **https:** scheme; it might have other schemes like **file:** (to retrieve a local file) or even relatively obscure schemes like **gopher:**.  One sneaky attack is to request one scheme (like “**gopher:**”) to a service that expects a completely different protocol; an attacker may be able to use this confusion to produce an attack.

* The “host” might not be what you expect; the host might refer to an arbitrary other computer or even the requesting computer.

* An attacker might provide **userinfo** (a user account name) and/or a port. The port, for example, allows a URL to request a connection on *any* port of a computer.

* A URL can even encode a variety of characters for any of this data.

If a server is fooled into requesting an inadequately checked URL, it is called a *server-side request forgery* (SSRF).

The main solution is to ensure that you greatly limit how you construct any URLs that you request. If possible, don’t use untrusted data to create these URLs. If you must use untrusted data to construct a URL (and this often occurs), maximally limit the URLs that can be constructed and ensure that only *safe* URLs can be constructed. For example, in many cases today you can limit the URL to a single scheme (**https:**), there is usually no need to allow (for example) ports or usernames.

Server-Side Request Forgery (SSRF) is such a common cause of security vulnerabilities that it is 2019 CWE Top 25 #30. It is [CWE-918](https://cwe.mitre.org/data/definitions/918.html).