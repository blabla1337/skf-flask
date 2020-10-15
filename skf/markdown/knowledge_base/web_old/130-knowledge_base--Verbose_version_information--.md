##Description:

Revealing system data or debugging information helps an adversary learn about the system
and form a plan of attack. An information leak occurs when system data or debugging
information leaves the program through an output stream or logging function.

##Mitigation:

Verify that the HTTP headers do not expose detailed version information of system components. For each different type of server, there are hardening guides dedicated especially for this type of data leaking. The same applies for i.e any other leak of version information such as the version of your programming language or other services running to make your application function.
