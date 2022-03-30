
# Question

Which of the followings requires for a succesful session termination? Can choose multiple answers.

* ( ) Availability of user interface controls that allow the user to manually log out.
* ( ) Session termination after a given amount of time without activity (session timeout).
* ( ) Proper invalidation of server-side session state.
* ( ) None of the above

-----SPLIT-----

# Answer

* (x) Availability of user interface controls that allow the user to manually log out.
* (x) Session termination after a given amount of time without activity (session timeout).
* (x) Proper invalidation of server-side session state.
* ( ) None of the above

-----SPLIT-----


# Question

Decide if the given statmen is true or false.

"Session termination can be performed securely when client-side session token is set to a new value."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* ( ) True
* (x) False

Explanation: It is a common mistake in session termination is that the client-side session token is set to a new value while the server-side state remains active and can be reused by setting the session cookie back to the previous value.

-----SPLIT-----