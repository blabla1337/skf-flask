
# Question

Whích of the following results may occur when a host header value is not valitated properly? Can choose multiple answers.

* ( ) Dispatch requests to the first virtual host on the list
* ( ) Perform a redirect to an attacker-controlled domain
* ( ) Perform web cache poisoning
* ( ) Manipulate password reset functionality
* ( ) Allow access to virtual hosts that were not intended to be externally accessible
* ( ) None of the above

-----SPLIT-----

# Answer

* (x) Dispatch requests to the first virtual host on the list
* (x) Perform a redirect to an attacker-controlled domain
* (x) Perform web cache poisoning
* (x) Manipulate password reset functionality
* (x) Allow access to virtual hosts that were not intended to be externally accessible
* ( ) None of the above

-----SPLIT-----


# Question

Decide if the given statmen is true or false.

"As a result of a web cache poisoning, manipualted/posinoed web-cache can be served to anyone who request the application."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* (x) True
* ( ) False

-----SPLIT-----


# Question

Decide if the given statmen is true or false.

"It may be possible to access to Intranet application by making a request from outside with by changing the host header to 'Host: intranet.example.org'"

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* (x) True
* ( ) False

Explanation: an organization may have a single webserver on their internal network, which hosts both their public website (on www.example.org) and their internal Intranet (on intranet.example.org, but that record only exists on the internal DNS server). Although it would not be possible to browse directly to intranet.example.org from outside the network (as the domain would not resolve), it may be possible to access to Intranet by making a request from outside with the following Host header:

Host: intranet.example.org

This could also be achieved by adding an entry for intranet.example.org to your hosts file with the public IP address of www.example.org, or by overriding DNS resolution in the testing tool.

-----SPLIT-----