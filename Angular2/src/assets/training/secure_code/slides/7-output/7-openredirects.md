### Open Redirects and Forwards

[Web application]

A web application should not accept user-controlled input that specifies a link to some site on a different server and then, without strict controls, use that link to do a redirect. A web application that does this has an *open redirect*.

This can be hard to understand, so let’s look at an example. Let’s imagine that a server-side web application has a “**/redirect**” link that accepts a parameter **url=**, and then simply redirects requests to the **url= value**. That means that an attacker could create an HTML file anywhere that looks like this (the example is based on text in MITRE’s text on [CWE-601](https://cwe.mitre.org/data/definitions/601.html)):

<b>&lt;a href=&quot;https&#58;//bank.example.com/redirect?url=https&#58;//attacker.example.net"&gt;Click here to log in&lt;/a&gt;</b>

What is the problem? The problem is that a user who checked the link would think that this link went to a trusted domain (e.g., **bank.example.com**). While technically that is true, when clicked, the supposedly trusted domain will quietly redirect the user to some other domain that might be dangerous and not what the user expected (e.g., **attacker.example.net**). More generally, the problem is that an open redirect can be used to fool humans and create stronger phishing attacks. Humans can be lulled into thinking they are going to a trusted domain, without realizing that they will in fact be immediately transferred to an untrusted domain. In theory, the users should also check *where they are now* on each page, but busy humans often don’t do that. We want to make it harder, not easier, to fool busy humans.

A related problem is a “forward”, where the web application forwards the request to some other part of the web application. The web application might incorrectly view the request as an *internal* request from the web application itself, instead of more accurately coming from an external user, and give it unwarranted privileges.

The [OWASP cheat sheet on unvalidated redirects and forwards](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) discusses various possible countermeasures:

* *“Simply avoid using redirects and forwards.*

* *If used, do not allow the URL as user input for the destination.*

* *Where possible, have the user provide [a] short name, ID or token which is mapped server-side to a full target URL.*

* *This provides the highest degree of protection against the attack tampering with the URL.*

* *Be careful that this doesn’t introduce an enumeration vulnerability where a user could cycle through IDs to find all possible redirect targets*

* *If user input can’t be avoided, ensure that the supplied value is valid, appropriate for the application, and is authorized for the user.*

* *Sanitize input by creating a list of trusted URLs (lists of hosts or a regex).*

* *This should be based on an allowlist approach, rather than a denylist.”*

Open redirects are such a common cause of security vulnerabilities that this weakness is 2019 CWE Top 25 #32. It is [CWE-601](https://cwe.mitre.org/data/definitions/601.html).