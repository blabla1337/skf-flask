# File inclusion attack
-------

## Description:

The File Inclusion vulnerability allows an attacker to include a file, usually exploiting
a "dynamic file inclusion" mechanisms implemented in the target application.
The vulnerability occurs due to the use of user-supplied input without proper validation.


This can lead to something as outputting the contents of the file, but depending on the
severity, it can also lead to:

- Code execution on the web server
- Code execution on the client-side such as JavaScript which can lead to other attacks
  such as cross-site scripting (XSS)
- Denial of Service (DoS)
- Sensitive Information Disclosure


Local File Inclusion (also known as LFI) is the process of including files, that are
already locally present on the server, through the exploiting of vulnerable inclusion
procedures implemented in the application. This vulnerability occurs, for example, when a
page receives, as input, the path to the file that has to be included and this input is
not properly sanitized, allowing directory traversal characters (such as dot-dot-slash)
to be injected. Although most examples point to vulnerable PHP scripts, we should keep
in mind that it is also common in other technologies such as JSP, ASP and others.

## Solution:

The most effective solution to eliminate file inclusion vulnerabilities is to avoid passing user-submitted input to any filesystem/framework API. If this is not possible the application can maintain a white list of files, that may be included on the page, and then use an identifier (for example the index number) to access the selected file. Any request containing an invalid identifier has to be rejected, in this way, there is no attack surface for malicious users to manipulate the path.

Also, disable the opportunity for the application to load remote resources. This is mostly achieved by adding a server configuration file such as php.ini or web.xml


