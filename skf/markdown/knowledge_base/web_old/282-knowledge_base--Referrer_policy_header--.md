##Description:
Requests made from a document, and for navigations away from that document
are associated with a Referer header. While the header can be suppressed for
links with the noreferrer link type, authors might wish to control the Referer
header more directly for a number of reasons,

- Privacy
A social networking site has a profile page for each of its users, 
and users add hyperlinks from their profile page to their favorite bands. 
The social networking site might not wish to leak the user’s profile URL 
to the band web sites when other users follow those hyperlinks 
(because the profile URLs might reveal the identity of the owner of the profile).

Some social networking sites, however, might wish to inform the band web sites that
the links originated from the social networking site but not reveal which specific
user’s profile contained the links.

- Security
A web application uses HTTPS and a URL-based session identifier. The web application might
wish to link to HTTPS resources on other web sites without leaking the user’s session 
identifier in the URL.

Alternatively, a web application may use URLs which themselves grant some capability. 
Controlling the referrer can help prevent these capability URLs from leaking via 
referrer headers.

Note that there are other ways for capability URLs to leak, and controlling 
the referrer is not enough to control all those potential leaks.

- Trackback
A blog hosted over HTTPS might wish to link to a blog hosted over HTTP and 
receive trackback links.

## Solution:

For more information about the policy and how it should be implemented please
visit the following link,

https://www.w3.org/TR/referrer-policy/#referrer-policies
