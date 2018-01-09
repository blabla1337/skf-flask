## Description:

Server Side Request Forgery (SSRF) attack, where an attacker abuse the functionality of a
vulnerable web application to send crafter request which which read or update internal 
resources. Attacker can attack an internal network or application behind the firewall with
this attack which is normally not accessible through external network and even attack the
internal network web applications.

SSRF attack can be used to make requests to other internal resources for accessing the 
metadata and to run a port can on the internal network. URL schema such as file:// can
be used to read the file from the server. Attackers can use legacy URL schemas such as 
dict, gopher, expect etc which can even cause remote code execution.

## Solution:

Disable unused URL schemas which are dangerous like expect://, file:///, ftp://, gopher://.
Proper whitelisting of domain or IP address which you need to access to. Response received from 
the internal server should not be shown to the attacker. Some services like Memcached, Redis, Elasticsearch and MongoDB do not require authentication by default, so we need to enable 
authentication for these services.
