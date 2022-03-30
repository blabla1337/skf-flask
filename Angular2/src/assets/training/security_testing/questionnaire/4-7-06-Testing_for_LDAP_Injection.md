
# Question

Decide if the given statmen is true or false.

"LDAP injection is a server-side attack, which could allow sensitive information about users and hosts represented in an LDAP structure to be disclosed, modified, or inserted."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* (x) True
* ( ) False

-----SPLIT-----

# Question

What might be the possible payload to bypass the following LDAP query?

'searchlogin= "(&(uid="+user+")(userPassword={MD5}"+base64(pack("H\*",md5(pass)))+"))";' 

* ( ) *)(uid=*))(|(uid=\*pass=password
* ( ) )(uid=\*)
* ( ) *)(uid=*))(|
* ( ) None of the above

-----SPLIT-----

# Answer

* (x) *)(uid=*))(|(uid=\*pass=password
* ( ) )(uid=\*)
* ( ) *)(uid=*))(|
* ( ) None of the above

Explanation: the search filter will results in: searchlogin="(&(uid=\*)(uid=\*))(|(uid=\*)(userPassword={MD5}X03MO1qnZdYdgyfeuILPmQ==))";

-----SPLIT-----