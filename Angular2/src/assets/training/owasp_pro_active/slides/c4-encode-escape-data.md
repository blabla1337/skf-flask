# C4: Encode and Escape Data

## Description

**Encoding** and escaping are defensive techniques meant to stop injection attacks. Encoding (commonly called "Output Encoding") involves translating special characters into some different but equivalent form that is no longer dangerous in the target interpreter, for example translating the ``<`` character into the ``&lt;`` string when writing to an HTML page. **Escaping** involves adding a special character before the character/string to avoid it being misinterpreted, for example, adding a ``\`` character before a ``"`` (double quote) character so that it is interpreted as text and not as closing a string.

Output encoding is best applied **just before** the content is passed to the target interpreter. If this defense is performed too early in the processing of a request then the encoding or escaping may interfere with the use of the content in other parts of the program. For example if you HTML escape content before storing that data in the database and the UI automatically escapes that data a second time then the content will not display properly due to being double escaped.

### Contextual Output Encoding

Contextual output encoding is a crucial security programming technique needed to stop XSS. This defense is performed on output, when you're building a user interface, at the last moment before untrusted data is dynamically added to HTML. The type of encoding will depend on the location (or context) in the document where data is being displayed or stored. The different types of encoding that would be used for building secure user interfaces includes HTML Entity Encoding, HTML Attribute Encoding, JavaScript Encoding, and URL Encoding.

#### Java Encoding Examples
For examples of the OWASP Java Encoder providing contextual output encoding see: [OWASP Java Encoder Project Examples](https://www.owasp.org/index.php/OWASP_Java_Encoder_Project#tab=Use_the_Java_Encoder_Project).


#### .NET Encoding Examples
Starting with .NET 4.5 , the Anti-Cross Site Scripting library is part of the framework, but not enabled by default. You can specify to use AntiXssEncoder from this library as the default encoder for your entire application using the web.conf settings. When applied is important to contextual encode your output - that means to use the right function from the AntiXSSEncoder library for the appropriate location of data in document.

#### PHP Encoding Examples
**Zend Framework 2**

In Zend Framework 2 (ZF2), ``Zend\Escaper`` can be used for encoding the output. For contextual encoding examples see [Context-specific escaping with zend-escaper](https://framework.zend.com/blog/2017-05-16-zend-escaper.html).

### Other Types of Encoding and Injection Defense
Encoding/Escaping can be used to neutralize content against other forms of injection. For example, it's possible to neutralize certain special meta-characters when adding input to an operating system command. This is called "OS command escaping", "shell escaping", or similar. This defense can be used to stop "Command Injection" vulnerabilities.

There are other forms of escaping that can be used to stop injection such as XML attribute escaping stopping various forms of XML and XML path injection, as well as LDAP distinguished name escaping that can be used to stop various forms of LDAP injection.

### Character Encoding and Canonicalization
Unicode Encoding is a method for storing characters with multiple bytes. Wherever input data is allowed, data can be entered using [Unicode](https://www.owasp.org/index.php/Unicode_Encoding) to disguise malicious code and permit a variety of attacks. [RFC 2279](https://tools.ietf.org/html/rfc2279) references many ways that text can be encoded.

Canonicalization is a method in which systems convert data into a simple or standard form.  Web applications commonly use character canonicalization to ensure all content is of the same character type when stored or displayed.

To be secure against canonicalization related attacks means an application should be safe when malformed Unicode and other malformed character representations are entered.


## Vulnerabilities Prevented
* [OWASP Top 10 2017 - A1: Injection](https://www.owasp.org/index.php/Top_10-2017_A1-Injection)
* [OWASP Top 10 2017 - A7: Cross Site Scripting (XSS)](https://www.owasp.org/index.php/Top_10-2017_A7-Cross-Site_Scripting_(XSS))
* [OWASP Mobile_Top_10_2014-M7 Client Side Injection](https://www.owasp.org/index.php/Mobile_Top_10_2014-M7)

## References
* [XSS](https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)) - General information
* [OWASP Cheat Sheet: XSS Prevention](https://www.owasp.org/index.php/XSS_(Cross_Site_Scripting)_Prevention_Cheat_Sheet) - Stopping XSS in your web application
* [OWASP Cheat Sheet: DOM based XSS Prevention](https://www.owasp.org/index.php/DOM_based_XSS_Prevention_Cheat_Sheet)
* [OWASP Cheat Sheet: Injection Prevention](https://www.owasp.org/index.php/Injection_Prevention_Cheat_Sheet)

## Tools
* [OWASP Java Encoder Project](https://www.owasp.org/index.php/OWASP_Java_Encoder_Project)
* [AntiXSSEncoder](https://docs.microsoft.com/en-us/dotnet/api/system.web.security.antixss.antixssencoder?redirectedfrom=MSDN&view=netframework-4.7.2)
* [Zend\Escaper](https://framework.zend.com/blog/2017-05-16-zend-escaper.html) - examples of contextual encoding
