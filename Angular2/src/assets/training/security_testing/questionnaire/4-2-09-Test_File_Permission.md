# Question

Decide if the given statmen is true or false.

"namei command can be used to recursively list file permissions."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* (x) True
* ( ) False

-----SPLIT-----


# Question

Decide if the given statmen is true or false.

"Some sensitive files, e.g. private key file, requeires restricted file permissions to operate."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* (x) True
* ( ) False

Explanation: SSH privte key file permissions need to be confired so that only the file owner can read and write.
-Octal form
chmod 600 ~/.ssh/id_rsa
-Equivalent literal form
chmod u=rw,go= ~/.ssh/id_rsa

-----SPLIT-----