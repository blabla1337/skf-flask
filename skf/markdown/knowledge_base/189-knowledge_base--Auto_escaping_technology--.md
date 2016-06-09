Auto escaping technology 
-------

**Description:**

Some frameworks/templates have the option to auto-escape all incoming user-input to harmless
encoded data in order to prevent attacks. However, this auto-escaping functionality is also
optional to be disabled. Whenever this auto-escaping function has been disabled your application
might be vulnerable to attacks like XSS.

**Solution:**

Whenever auto-escaping functionality in your application has been disabled for whatever reason, you
should make sure there is other protection in place like a HTML sanitizer in order to
prevent attackers from injecting malicious code into your application.

