### Same-Origin Policy and Cross-Origin Resource Sharing (CORS)

[Web Application]

When a web browser gets an HTML file, the HTML file is allowed to freely refer to images, videos, CSS stylesheets, and scripts to run. Normally the web browser will attempt to retrieve and use them, regardless of what website those materials come from.

However, when a web browser retrieves and runs a script (such as JavaScript), it would be dangerous for the web browser to allow that script to easily interact with arbitrary websites. If that were allowed, a malicious script could surreptitiously send private data to any other site, and the script could also attack other websites (e.g., by exploiting vulnerabilities or launching a DDoS attack).

To prevent many security problems, web browsers normally enforce on client-side JavaScript programs a set of rules called the *same-origin policy*. Under the same-origin policy, client-side JavaScript programs are only allowed to interact with the same *origin*, including viewing any resources. The origin of a URL is the combination of the protocol (usually https), port (443 by default for https), and host. Thus, **https://example.com/foo** and **https://example.com/bar** are considered to have the same origin because they have the combination (https, 443, example.com). The purpose of the same-origin policy is to isolate potentially malicious documents (Mozilla, [*Same-Origin Policy*](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)).

The same-origin policy prevents many security issues, but it is sometimes too strict. A website can specifically allow interaction by JavaScript from other origins by using Cross-Origin Resource Sharing (CORS). CORS can be useful, since it relaxes the restrictions of the same-origin policy. CORS can also be a problem, since CORS can enable vulnerabilities if it is poorly used. CORS is specified in great detail in the [WHATWG Fetch specification](https://fetch.spec.whatwg.org/#http-extensions). Mozilla has a nice description of CORS in their [documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS). In this unit, we will briefly cover the highlights, summarizing some of the material from the Mozilla CORS documentation.

In brief: CORS allows web servers to declare what other origins are allowed access to what resources (URLs), and which HTTP verbs (**GET**, **POST**, **DELETE**, etc.) are permitted to those other origins. Web browsers request this information and use it to determine if client-side JavaScript programs are allowed to make a cross-origin request (that is, an action outside their origin). This information is exchanged using new HTTP headers that are output by the web browser and web server. CORS requests are used for cross-origin **XMLHttpRequest** and **Fetch** requests (among other circumstances).

There are two kinds of CORS requests, a (so-called) *simple request* and a *preflighted request*. This is an optimization. Simple requests use a single interaction, while successful preflighted requests use two interactions. Any CORS request that cannot be done with a simple request is automatically implemented by the web browser with a preflighted request. Preflighted requests have more latency than a simple request, so where you *can*, write your client-side code so it will use CORS simple requests. Sometimes that is not possible, and then a higher-latency preflighted request will automatically be used.

A CORS simple request is used when *all* of the following are true:

* The requested method is **GET**, **HEAD**, or **POST**

* The request headers are only the ones automatically set by the web browser (aka user agent), optionally extended with *CORS-safelisted request-headers*. Examples of these safelisted headers are **Accept**, **Accept-Language**, **Content-Language**, **Viewport-Width**, and **Width**.

* The **Content-Type** header is one of: **application/x-www-form-urlencoded**, **multipart/form-data**, or **text/plain**.

* A few other requirements are also met. See the specification for details; in most cases these other requirements will be met.

When a CORS simple request is made, the web browser makes the request as usual and also sets the HTTP header **Origin** to the script origin. The web server then determines if that request is acceptable. The web server then replies and sets the HTTP header **Access-Control-Allow-Origin** with information about the allowed origin(s). If that value is “**&#42;**”, then *any* origin is allowed that access. The web browser looks at the **Access-Control-Allow-Origin**, and if the requesting origin matches, the script receives any information returned.

A preflighted request, unlike a simple request, uses an extra step. In a preflighted request, the web browser first sends an **OPTIONS** request with the **Origin** and other information, to ask the web server if the actual request is “*safe to send*”. If the web server approves it, then the actual request is sent. Some browsers do not follow redirects for a preflighted request; see the [Mozilla CORS documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) for solutions if it matters to you.

By default, browsers will not send credentials (cookies and HTTP Authentication information) in a CORS request. However, a specific flag can be set on an  **XMLHttpRequest** object or **Request** constructor to send credentials. If this is done, the web server must return **Access-Control-Allow-Credentials: true** or the JavaScript program will not receive the results. Web servers should be very cautious about using this; if it is used at all, be very picky about the origins allowed. It is much safer to *not* use **Access-Control-Allow-Credentials**, as this allows credentialed programmatic control from a different origin.

If you intend for some information to be publicly readable on your web server, and it never varies (no matter who requested it or where it is from), consider returning “**Access-Control-Allow-Origin: &#42;**” when a web browser tries to **GET** that information. This allows client-side JavaScript programs to directly retrieve that information and use it further. That does allow JavaScript programs to repeatedly request it, so in theory that makes DDoS attacks slightly easier. However, for many websites the goal is to distribute some information, and DDoS can be countered in other ways.

Sometimes the information may vary depending on the origin of the requestor (this is true if you set an **Access-Control-Allow-Origin** to any value other than “**&#42;**”). In these cases, ensure that you include a “**Vary**” header with the value “**Origin**”. This “**Vary**” value tells the web browser that the result may vary depending on the origin, preventing information from one origin from leaking into another origin (or lack of origin) via CORS.

Details on how to enable CORS for a large variety of circumstances is available at [enable-cors.org](https://enable-cors.org/). You can also check out the following resources for more details:

* [Web Hypertext Application Technology Working Group (WHATWG). ](https://fetch.spec.whatwg.org/)[*Fetch*](https://fetch.spec.whatwg.org/) 

* [Mozilla’s ](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)[*Same-origin policy*](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)[ documentation](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy) 

* [Mozilla’s Cross-Origin Resource Sharing (CORS) documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).
