# C5: Validate All Inputs

## Description
Input validation is a programming technique that ensures only properly formatted data may enter a software system component.

### Syntax and Semantic Validity
An application should check that data is both *syntactically* and *semantically* valid (in that order) before using it in any way (including displaying it back to the user).

**Syntax validity** means that the data is in the form that is expected. For example, an application may allow a user to select a four-digit "account ID" to perform some kind of operation. The application should assume the user is entering a SQL injection payload, and should check that the data entered by the user is exactly four digits in length, and consists only of numbers (in addition to utilizing proper query parameterization).

**Semantic validity** includes only accepting input that is within an acceptable range for the given application functionality and context. For example, a start date must be before an end date when choosing date ranges.

### Allowlisting vs Denylisting
There are two general approaches to performing input syntax validation, commonly known as allow and deny lists:

* **Denylisting** or **denylist validation*** attempts to check that given data does not contain "known bad" content. For example, a web application may block input that contains the exact text ``<SCRIPT>`` in order to help prevent XSS. However, this defense could be evaded with a lower case script tag or a script tag of mixed case.
* **Allowlisting** or **allowlist** validation attempts to check that a given data matches a set of "known good" rules. For example a allowlist validation rule for a US state would be a 2-letter code that is only one of the valid US states.

**Important**
When building secure software, allowlisting is the recommended minimal approach. Denylisting is prone to error and can be bypassed with various evasion techniques and can be dangerous when depended on by itself. Even though denylisting can often be evaded it can often useful to help detect obvious attacks. So while **allowlisting** helps limit the attack surface by ensuring data is of the right syntactic and semantic validity, **denylisting** helps detect and potentially stop obvious attacks.

### Client side and Server side Validation
Input validation must always be done on the server-side for security. While client side validation can be useful for both functional and some security purposes it can often be easily bypassed. This makes server-side validation even more fundamental to security. For example, JavaScript validation may alert the user that a particular field must consist of numbers but the server side application must validate that the submitted data only consists of numbers in the appropriate numerical range for that feature.

### Regular Expressions
Regular expressions offer a way to checkwhether data matches a specific pattern. Let’s start with a basic example.

The following regular expression is used to define a allowlist rule to validate usernames.

    ^[a-z0-9_]{3,16}$

This regular expression allows only lowercase letters, numbers and the underscore character. The username is also restricted to a length of 3 and 16 characters.

**Caution: Potential for Denial of Service**

Care should be exercised when creating regular expressions. Poorly designed expressions may result in potential denial of service conditions (aka [ReDoS](https://www.owasp.org/index.php/Regular_expression_Denial_of_Service_-_ReDoS) ). Various tools can test to verify that regular expressions are not vulnerable to ReDoS.

**Caution: Complexity**

Regular expressions are just one way to accomplish validation. Regular expressions can be difficult to maintain or understand for some developers. Other validation alternatives involve writing validation methods programmatically which can be easier to maintain for some developers.


### Limits of Input Validation

**Input validation does not always make data "safe" since certain forms of complex input may be "valid" but still dangerous. For example a valid email address may contain a SQL injection attack or a valid URL may contain a Cross Site Scripting attack**. Additional defenses besides input validation should always be applied to data such as query parameterization or escaping.

### Challenges of Validating Serialized Data
Some forms of input are so complex that validation can only minimally protect the application. For example, it's dangerous to deserialize untrusted data or data that can be manipulated by an attacker. The only safe architectural pattern is to not accept serialized objects from untrusted sources or to only deserialize in limited capacity for only simple data types. You should avoid processing serialized data formats and use easier to defend formats such as JSON when possible.

If that is not possible then consider a series of validation defenses when processing serialized data.
* Implement integrity checks or encryption of the serialized objects to prevent hostile object creation or data tampering.
* Enforce strict type constraints during deserialization before object creation; typically code is expecting a definable set of classes. Bypasses to this technique have been demonstrated.
* Isolate code that deserializes, such that it runs in very low privilege environments, such as temporary containers.
* Log security deserialization exceptions and failures, such as where the incoming type is not the expected type, or the deserialization throws exceptions.
* Restrict or monitor incoming and outgoing network connectivity from containers or servers that deserialize.
* Monitor deserialization, alerting if a user deserializes constantly.


### Unexpected User Input (Mass Assignment)
Some frameworks support automatic binding of HTTP requests parameters to server-side objects used by the application. This auto-binding feature can allow an attacker to update server-side objects that were not meant to be modified. The attacker can possibly modify their access control level or circumvent the intended business logic of the application with this feature.

This attack has a number of names including: mass assignment, autobinding and object injection.

As a simple example, if the user object has a field privilege which specifies the user's privilege level in the application, a malicious user can look for pages where user data is modified and add privilege=admin to the HTTP parameters sent.  If auto-binding is enabled in an insecure fashion, the server-side object representing the user will be modified accordingly.

Two approaches can be used to handle this:
* Avoid binding input directly and use Data Transfer Objects (DTOs) instead.
* Enable auto-binding but set up allowlist rules for each page or feature to define which fields are allowed to be auto-bound.

More examples are available in the [OWASP Mass Assignment Cheat Sheet](https://www.owasp.org/index.php/Mass_Assignment_Cheat_Sheet).

### Validating and Sanitizing HTML
Consider an application that needs to accept HTML from users (via a WYSIWYG editor that represents content as HTML or features that directly accept HTML in input). In this situation validation or escaping will not help.

* Regular expressions are not expressive enough to understand the complexity of HTML5.
* Encoding or escaping HTML will not help since it will cause the HTML to not render properly.

Therefore, you need a library that can parse and clean HTML formatted text. Please see the [XSS Prevention Cheat Sheet on HTML Sanitization](https://www.owasp.org/index.php/XSS_(Cross_Site_Scripting)_Prevention_Cheat_Sheet#RULE_.236_-_Sanitize_HTML_Markup_with_a_Library_Designed_for_the_Job) for more information on HTML Sanitization.

### Validation Functionality in Libraries and Frameworks
All languages and most frameworks provide validation libraries or functions which should be leveraged to validate data. Validation libraries typically cover common data types, length requirements, integer ranges, "is null" checks and more. Many validation libraries and frameworks allow you to define your own regular expression or logic for custom validation in a way that allows the programmer to leverage that functionality throughout your application. Examples of validation functionality include PHP’s [filter functions](https://secure.php.net/manual/en/filter.examples.validation.php) or the [Hibernate Validator](http://hibernate.org/validator/) for Java. Examples of HTML Sanitizers include [Ruby on Rails sanitize method](http://edgeapi.rubyonrails.org/classes/ActionView/Helpers/SanitizeHelper.html), [OWASP Java HTML Sanitizer](https://www.owasp.org/index.php/OWASP_Java_HTML_Sanitizer_Project) or [DOMPurify](https://github.com/cure53/DOMPurify).

## Vulnerabilities Prevented
* Input validation reduces the attack surface of applications and can sometimes make attacks more difficult against an application.
* Input validation is a technique that provides security to certain forms of data, specific to certain attacks and cannot be reliably applied as a general security rule.
* Input validation should not be used as the primary method of preventing [XSS](https://www.owasp.org/index.php/XSS_(Cross_Site_Scripting)_Prevention_Cheat_Sheet), [SQL Injection](https://www.owasp.org/index.php/SQL_Injection_Prevention_Cheat_Sheet) and other attacks.

## References
* [OWASP Cheat Sheet: Input Validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
* [OWASP Cheat Sheet: iOS - Security Decisions via Untrusted Inputs](https://www.owasp.org/index.php/IOS_Developer_Cheat_Sheet#Security_Decisions_via_Untrusted_Inputs_.28M7.29)
* [OWASP Testing Guide: Testing for Input Validation](https://www.owasp.org/index.php/Testing_for_Input_Validation)

## Tools
* [OWASP Java HTML Sanitizer Project](https://www.owasp.org/index.php/OWASP_Java_HTML_Sanitizer)
* [Java JSR-303/JSR-349 Bean Validation](http://beanvalidation.org/)
* [Java Hibernate Validator](http://hibernate.org/validator/)
* [JEP-290 Filter Incoming Serialization Data](http://openjdk.java.net/jeps/290)
* [Apache Commons Validator](https://commons.apache.org/proper/commons-validator/)
* PHP’s [filter functions](https://secure.php.net/manual/en/book.filter.php)
