# Directory listing
-------

## Description:

Whenever directory listing is enabled an attacker could gain sensitive information about
the systems hierarchical structure and gain knowledge about directories or files which should
possibly not be publicly accessible. An attacker could use this information to
increase his attack vector. In some cases this could even lead to an attacker gaining knowledge about
credentials or old vulnerable system demo functions which might lead to remote code execution.


## Solution:

Different types of servers require a different type of approach in order to disable
directory listing. For instance: apache uses a .htacces in order to disable directory listing.
As in iis7 directory listing is disabled by default.
