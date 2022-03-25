### Other HTTP Hardening Headers

[Web application]

When you are delivering web pages you can limit what can be done with the results, making it harder for attackers to cause serious damage. In short, there are other HTTP headers that you can set that can sometimes harden your applications against attacks. We have already discussed the Content Security Policy (CSP), which is perhaps the most important one. Here are some other HTTP headers you should consider using:

* **X-Content-Type-Options**
This should be set to **nosniff**, which means that the MIME types provided are correct and that the receiver should not try to guess what the type is. This means that attackers won’t be able to fool the web browser into using a different type.

* **X-Frame-Options**
This should be set to **DENY** or **SAMEORIGIN**. Like the CSP **frame-ancestors**, this prevents the use of frames or only allows them from the origin, countering many clickjacking attacks. Technically, X-Frame-Options has been obsoleted by CSP **frame-ancestors**, but if you might have Internet Explorer (IE) users, you also need this as IE does not support CSP **frame-ancestors**.

* **HTTP Strict-Transport-Security (HSTS)**
This means that *only* the secured HTTPS protocol, and not the insecure HTTP protocol, is permitted for future visits to this site for a given number of seconds. A common setting is “**Strict-Transport-Security: max-age=31536000;**” which means that *only* HTTPS will be allowed for a year (the number is the number of seconds). A larger number is fine.

If your site is publicly accessible, you can easily test your headers using the [Security Headers website](https://securityheaders.com/).

Also, an important word about HTTP headers in general. You may decide, for various reasons, to provide other HTTP headers. If some of that header information might be from an attacker, be *especially careful*. As always, do very careful input validation. There is a nasty attack, in particular, where the attacker manages to insert a newline in the input; this will cause *HTTP header splitting* in HTTP versions 1.1 and 2, where the rest of the text after the newline may be interpreted as an HTTP header provided by the attacker. This could disable many protections or even implement an attack.