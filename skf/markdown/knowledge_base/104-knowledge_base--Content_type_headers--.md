# Content type headers
-------

## Description:

Setting the right content headers is important for hardening your applications security,
this reduces exposure to drive-by download attacks or sites serving user uploaded
content that, by clever naming could be treated by MS Internet Explorer as executable or
dynamic HTML files and thus can lead to security vulnerabilities.


## Solution:

An example of a content type header would be:  

    Content-Type: text/html; charset=UTF-8
    or:
    Content-Type: application/json;
