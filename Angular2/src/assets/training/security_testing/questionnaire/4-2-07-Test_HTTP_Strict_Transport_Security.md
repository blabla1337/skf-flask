# Question

Decide if the given statmen is true or false.

"The HTTP Strict Transport Security (HSTS) feature lets a web application inform the browser through the use of a special response header that it should never establish a connection to the specified domain servers using un-encrypted HTTP"

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* (x) True
* ( ) False

-----SPLIT-----

# Question

What happens if a user uses a web browsers does not support HSTS header, even though your server provide HSTS header on the response headers? Can choose multiple answers.

* ( ) The user will be vulnerable to HTTPS downgrade attack.
* ( ) There will be no effect on their browsing experince in terms of functionality, still can use the website.
* ( ) The user will not even able to visit the website.
* ( ) None of the above 

-----SPLIT-----

# Answer

* (x) The user will be vulnerable to HTTPS downgrade attack.
* (x) There will be no effect on their browsing experince in terms of functionality, still can use the website.
* ( ) The user will not even able to visit the website.
* ( ) None of the above 

Explanation: HSTS header inform the browser to enable extra securities to protect users against HTTPS downgrade or MiTM attacks. If the browser does not provide such extra security, it will not affect visiting the website or prevent users to access the website.


-----SPLIT-----

Which of the following directives supported by HSTS header? Can choose multiple answers.


* ( ) max-age
* ( ) includeSubDomains
* ( ) preload
* ( ) None of the above 

-----SPLIT-----

# Answer

* (x) max-age
* (x) includeSubDomains
* (x) preload
* ( ) None of the above 

Explanation: max-age and includeSubDomains officially supported, whereas preload is Unofficial: to indicate that the domain(s) are on the preload list(s) and that browsers should never connect without HTTPS. This is supported by all major browsers but is not official part of the specification. (See hstspreload.org for more information.)