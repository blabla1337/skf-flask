##Description:

Authors of services which use the HTTP protocol SHOULD NOT use GET-based forms for the
submission of sensitive data, because this will cause this data to be
encoded in the Request-URI. Many existing servers, proxies,
and browsers will log the request URL in some place where it might be
visible to third parties. Servers can use POST-based form submission instead.
GET parameters are also more likely to be vulnerable to XSS. Please refer to the
XSS manual in the knowledge base for more information.

##Mitigation:

Whenever transmitting sensitive data always do this by means of the POST request or by header.
Note: Avoid user-input in your application header, this could lead to vulnerabilities.
Also make sure you disable all other HTTP request methods which are unnecessary for
your applications operation such as; REST, PUT, TRACE, DELETE, OPTIONS, etc, since
allowing these request methods could lead to vulnerabilities and injections.
