# XSS injection
-------

## Description:

Every time the application gets user-input, whether this showing it on screen or processing
this data in the application background, these parameters should be escaped for malicious
code in order to prevent cross-site scripting injections.
When an attacker gains the possibility to perform an XSS injection,
he is given the opportunity to inject HTML and JavaScript code directly into the
application. This could lead to accounts being compromised by stealing session cookies or directly affect the operation of the target application.

## Solution:

In order to prevent XSS injections, all user-input should be escaped or encoded.
You could start by sanitizing user-input as soon as it is inserted into the application,
by preference using a so called whitelisting method.
This means you should not check for malicious content like the tags or anything,
but only allow the expected input. Every input which is outside of the intended operation
of the application should immediately be detected and log-in rejected.

The second step would be encoding all the parameters or user-input before putting this in
your html with encoding libraries specially designed for this purpose.

You should take into consideration that there are several contexts for encoding user-input for
escaping XSS injections. These contexts are amongst others:

HTML encoding is for whenever your user-input is displayed directly into your HTML.
HTML attribute encoding is the type of encoding/escaping that should be applied whenever your user input is displayed into the attribute of your HTML tags.
HTML URL encoding ;This type of encoding/escaping should be applied to whenever you are using user-input into a HREF tag.

JavaScript encoding should be used whenever parameters are rendered via JavaScript; your application will detect normal injections in the first instant. But your application still remains vulnerable to JavaScript encoding which will not be detected by the normal encoding/escaping methods.

