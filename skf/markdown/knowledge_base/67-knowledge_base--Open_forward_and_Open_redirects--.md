# Open forward and Open redirects
-------

## Description:

Unvalidated redirects and forwards are possible when a web application accepts untrusted
input that could cause the web application to redirect the request to a URL contained
within the untrusted input. By modifying untrusted URL input to a malicious site, an attacker
may successfully launch a phishing scam and steal user credentials. Because the server
name in the modified link is identical to the original site, phishing attempts may have
a more trustworthy appearance. Unvalidated redirect and forward attacks can also be used
to maliciously craft a URL that would pass the application's access control check and
then forward the attacker to privileged functions that they would normally not be able
to access.

## Solution:

Use a whitelisting method for determining where the user should be redirected towards.
You could also show a warning when redirecting to potentially untrusted content.
