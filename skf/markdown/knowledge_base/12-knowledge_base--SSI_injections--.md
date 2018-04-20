## Description:

Web servers usually give developers the ability to add small pieces of dynamic code inside
static HTML pages, without having to deal with full-fledged server-side
or client-side languages.

This feature is incarnated by the Server-Side Includes (SSI).
The attacker will try to inject code into the application that will
be interpreted by SSI mechanisms. A successful exploitation of this vulnerability
allows an attacker to inject code into HTML pages or even perform remote code execution.

## Solution:

The SSI handler on the web-server should not be activated when it is not used.
