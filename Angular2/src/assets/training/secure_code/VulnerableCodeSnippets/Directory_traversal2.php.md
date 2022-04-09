# Question
 
What is the problem here?
 
```
<?php
$template = 'lang.php';

if (isset($_GET['Submit'])) {
   $userName = $_GET['userName'];
   $userName = stripslashes($userName);
   $userName = mysql_real_escape_string($userName);

   if (is_numeric($userName)){ 
      $userID = "SELECT userID FROM users WHERE user_name = '$userName'";
      $result = mysql_query($userID) or die('<H3>No record or a problem has occurred</H3>');
      if (mysql_num_rows($result) > 0){
         echo "Welcome $userName";
   }}}
   
if ( is_set( $_COOKIE['languageTemplate'] ) )
   $languageTemplate = $_COOKIE['languageTemplate'];
include ( "/tmp/langtemplates/" . $languageTemplate ); 
?>
```
 
-----SPLIT-----
 
# Answer

It is a Directory Traversal issue. 'languageTemplate' is not sanitized for file inclusion. 'Cookie: languageTemplate=../../etc/passwd' may return the file content.