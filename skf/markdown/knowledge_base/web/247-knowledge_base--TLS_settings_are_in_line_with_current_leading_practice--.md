## Description:

TLS settings must always be in line with current leading practice. Whenever TLS
settings and ciphers get outdated, the TLS connection can be degraded/broken and used by
attackers to eavesdrop on users traffic over the application.

## Solution:

There should be structural scans that are done regularly against the applications TLS settings
and configurations to check whether the TLS settings are in line with current leading practice.

This could be achieved by using the SSLLabs api or the OWASP O-Saft project.

O-Saft is an easy to use tool to show informations about SSL certificate and tests the SSL 
connection according to a given list of ciphers and various SSL configurations.

It's designed to be used by penetration testers, security auditors or server administrators. 
The idea is to show the important information or the special checks with a simple call of the tool.
However, it provides a wide range of options so that it can be used for comprehensive and special 
checks by experienced people.

While doing these tests also take into consideration the following configuration on the server
side:

Verify that old versions of SSL and TLS protocols, algorithms, ciphers, and configuration are 
disabled, such as SSLv2, SSLv3, or TLS 1.0 and TLS 1.1. The latest version of TLS should be the 
preferred cipher suite.

