# Question
 
What is the problem here?
 
```
<?php
	$connectInfo = ldap_connect("localhost");
	$userInfo = $_GET['userInfo'];
	$criteria = "(&(objectclass=person)(userName=*)(userAddress=*)(|(uid={$userInfo})(cn={$userInfo})))";
	$results=ldap_search($connectInfo, $userInfo, $userInfo, $criteria);
	$info = ldap_get_entries($connectInfo, $results);
	echo $info["count"]." records returned";
?>
```
 
-----SPLIT-----
 
# Answer

It is an LDAP Injection issue. 'userInfo' parameter is not being checked for any malicious LDAP chars and it is used in search function directly. The attacker can inject LDAP special chars to bypass restrictions. 
