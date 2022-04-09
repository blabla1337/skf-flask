# Question
 
What is the problem here?
 
```
<?php
   $template = 'blue.php';
   if ( is_set( $_COOKIE['TEMPLATE'] ) )
      $template = $_COOKIE['TEMPLATE'];
   include ( "/home/users/phpguru/templates/" . $template );
?>
```
 
-----SPLIT-----
 
# Answer

It is a Directory Traversal issue. The user can include files without restrictions. For example: 'Cookie: TEMPLATE=../../../../../../../../../etc/passwd' may return the file content. https://owasp.org/www-community/attacks/Path_Traversal