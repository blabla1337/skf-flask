Servers must not be trusted without explicit authentication
-------

**Description:**

Whenever the server your web-application is connecting towards is not using any form of
explicit authentication and is internet facing then this results into that the server
cannot be trusted. This is because the server can be potentially be owned and managed by
everybody including hackers.


**Solution:**

Whenever the web-application is facing the internet third parties trying to
access it should always use a form of authentication in order to gain access.
