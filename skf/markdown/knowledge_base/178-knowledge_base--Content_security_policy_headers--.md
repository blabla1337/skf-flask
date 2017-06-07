# Content security policy headers
-------

## Description:

The main use of the content security policy header is to, detect, report, and reject XSS attacks. The core issue in relation to XSS attacks is the browser's inability to distinguish between a script that's intended to be part of your application, and a script that's been maliciously injected by a third-party.
With the use of CSP(Content Security policy), we can tell the browser which script is safe to execute and which scripts are most likely been injected by an attacker.

## Solution:

A best practice for implementing CSP in your application would be to externalize all
JavaScript within the web pages.

So this:
    <script>
      function doSomething() {
        alert('Something!');
      }
	</script>

	<button onclick='doSomething();'>foobar!</button>

Must become this:
	<script src='doSomething.js'></script>
	<button id='somethingToDo'>Let's foobar!</button>

The header for this code could look something like:
    Content-Security-Policy: default-src'self'; object-src'none'; script-src'https://mycdn.com'

Since it is not entirely realistic to implement all JavaScript on external pages we can apply sort of a cross-site request forgery token to your inline JavaScript. This way the browser can again distinguish the difference between code which is part of the application against probable malicious injected code, in CSP this is called the 'nonce'. Of course, this method is also very applicable on your existing code and designs.
Now, to use this nonce you have to supply your inline script tags with the nonce attribute. Firstly, it's important that the nonce changes for each response. Otherwise, the nonce would become guessable. So it should also contain a high entropy and should be hard to predict. Similar to the operation of the CSRF tokens, the nonce becomes impossible for the attacker to predict making it difficult to execute a successful XSS attack.


Inline JavaScript example containing nonce:
	<script nonce=sfsdf03nceI23wlsgle9h3sdd21>
    <!-- Your javscript code -->
    </script>

Matching header example:
    Content-Security-Policy: script-src 'nonce-sfsdf03nceI23wlsgle9h3sdd21'

There is a whole lot more to learn about the CSP header for in-depth implementation in your application. This knowledge base item just scratches the surface and it would be highly recommended to gain more in-depth knowledge about this powerful header

## Very Important:
When applying the CSP header, although it blocks XSS attacks. Your
application still remains vulnerable to HTML and other code injections.
So this is not a substitute for, validation, sanitizing and encoding of user-input.
