# Question
 
What is the problem here?
 
```
<?php 
$userName=$_POST['userName'];
$userPass=$_POST['userPassword'];

if($_GET['action']=='registration'){
  $contenttowrite = $contenttowrite.'<tr><td colspan="2">The feature is still in progress</td></tr>';
}
else if($_GET['action']=='login'){
  $connStr = mysql_connect("localhost", "root", "secPass1907");
  if (!$connStr) die ("Opps service is not reachable!");
  mysql_select_db("school", $connStr) or die ("Opps service is not reachable!");
  $queryResult = mysql_query("SELECT * FROM users WHERE u_name='$userName' AND `u_passwd`='$userPass'",$connStr);
  $result = mysql_fetch_array ($queryResult);
}
?>
```
 
-----SPLIT-----
 
# Answer

It is an SQL Injection issue. 'userName' and 'userPass' parameters are vulnerable for injection attacks. These parameters are being retrieved from the request and concatenated to build a SQL query.