Sanitize unstructured data 
-------

**Description:**

Verify that unstructured data is sanitized to enforce generic safety measures. When this is not
setup an attacker can use this unstructured data to harm the application and perform injections.

**Solution:**

Unstructured data needs to be sanitized to enforce generic safety measures for example:

- allowed characters
- character length, 

Also some characters are potentially harmful in given context and thus should be escaped. 
(e.g. natural names with Unicode or apostrophes, such as &#x306D;&#x3053; or O'Hara)
