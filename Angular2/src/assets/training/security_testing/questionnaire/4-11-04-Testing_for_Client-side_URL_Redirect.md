
# Question

Decide if the given statmen is true or false.

"Client-side URL Redirect (open redirection) is an input validation flaw that exists when an application accepts user-controlled input that specifies a link which leads to an external URL that could be malicious."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* (x) True
* ( ) False


-----SPLIT-----


# Question

Decide if the given statmen is true or false.

"Considering the code snippets below, an attacker could redirect the victim to a malicious site simply by submitting the following query string: 'http://www.victim.site/?#www.malicious.site'"

var redir = location.hash.substring(1);
if (redir) {
    window.location=decodeURIComponent(redir);
}


* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* (x) True
* ( ) False


-----SPLIT-----

