
Robots.txt
-------

**Description:**

Each site uses a robots.txt file which allows search engines to provide information. 
The robots.txt determines what pages may or may not be indexed by google or yahoo etc. 
However, a common mistake made by programmers is applying a blacklisting method causing 
the application displaying sensitive information to attackers.


**Solution:**

instead of the blacklisting method:

User-agent: * 
Disallow: /squirrelmail/
Disallow: /admin/
Disallow: /modules/

you should use a whitelisting method:

User-agent: * 
Disallow: * 
Allow: /index.html
Allow: /home.html

	