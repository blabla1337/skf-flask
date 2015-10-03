
Directory listing
-------

**Description:**

Whenever directory listing is enabled an attacker could gain sensitive information about 
the systems hierarchical structure and gain knowledge about directories which should 
possibly not be publicly accessible. An attacker could use this information to 
increase his attack vector.


**Solution:**

Different types of servers require a different type of approach in order to disable 
directory listing. for instance: apache uses a .htacces in order to disable directory listing.
As in iis7 directory listing is disabled by default. 

	