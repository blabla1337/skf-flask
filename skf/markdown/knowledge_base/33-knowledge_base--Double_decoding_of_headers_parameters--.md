# Double decoding of headers/parameters
-------

## Description:

Double decoding is a problem which often occurs when multiple servers are used in which a
configuration error is made.
A hacker can encode his payload differently so it will not be recognized by an WAF or IDS
and also bypass the escaping of the application.

By using double encoding it's possible to bypass security filters that only decode user
input once. The second decoding process is executed by the backend platform or modules
that properly handle encoded data, but don't have the corresponding security checks in
place.

Attackers can inject double encoding in pathnames or query strings to bypass the
authentication schema and security filters in use by the web application.

## Solution:

Only one web-server should decode/encode the data.
