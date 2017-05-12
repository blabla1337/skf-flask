# Include anti-caching headers
-------

## Description:

Anti-caching headers have the ability to tell the browser,
computer and proxies what information they may or may not store on the intermediate media

## Solution:

These headers are also known as the: Cache-control: no-store,no-cache and provide
protection of sensitive information when implemented in the application or web-server.

Rightly configured anti caching headers will look like the following as a response

	Expires: Tue, 03 Jul 2001 06:00:00 GMT
	Last-Modified: {now} GMT
	Cache-Control: no-store, no-cache, must-revalidate, max-age=0
	Cache-Control: post-check=0, pre-check=0
	Pragma: no-cache
