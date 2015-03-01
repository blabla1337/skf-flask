
Robots.txt
-------

**Description:**

Each site uses a robots.txt file which allows search engines to provide information. tThe robots.txt determins what pages may or may not be indexed by google or yahoo etc. However, a common mistake made by programmers is applying a blacklisting method causing the application displaying sensitive information to attackers.


**Solution:**

instead of the blacklisting method:

User-agent: * <br>
Disallow: /squirrelmail/<br>
Disallow: /admin/<br>
Disallow: /modules/<br>

you should use a whitelisting mehod:

User-agent: * <br>
Disallow: * <br>
Allow: /index.html<br>
Allow: /home.html<br>

	