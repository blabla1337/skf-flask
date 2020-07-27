##Description:

Cross-Site Request Forgery (CSRF) is a type of attack that occurs when a malicious Web site,
email, blog, instant message, or program causes a users Web browser to perform an unwanted
action on a trusted site for which the user is currently authenticated.

The impact of a successful cross-site request forgery attack is limited to the
capabilities exposed by the vulnerable application. For example, this attack could result
in a transfer of funds, changing a password, or purchasing an item in the users context.
In effect, CSRF attacks are used by an attacker to make a target system perform a
function (funds Transfer, form submission etc.) via the targets browser without
knowledge of the target user at least until the unauthorized function has been committed.

## Solution:

REST (REpresentational State Transfer) is a simple stateless architecture that generally runs
over HTTPS/TLS. The REST style emphasizes that interactions between clients and services are
enhanced by having a limited number of operations

Since the architecture is stateless, the application should make use of sessions or cookies to
store the HTTP sessions, which allow associating information with individual visitors. The preferred method for REST
services is to utilize tokens for interactive information interchange between the user and the server. 

By sending this information solely by means of headers, the application is no longer susceptible to CSRF attacks
since the CSRF attack utilizes the browsers cookie jar for succesful attacks.
