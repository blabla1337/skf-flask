# Question
 
What is the problem here?
 
```
<?php
class UserClass
{
   public $user_user_cache_file;
   public $user_doc;
   public $user_path;

   function __construct($user_doc, $user_path) {
    $this->name = $name;
    $this->color = $color;
   }
   
   function __destruct()
   {
      $file = "/var/www/cache/tmp/{$this->user_cache_file}";
      if (file_exists($file)) @unlink($file);
   }

   function get_doc() {
    return $this->user_doc;
   }
   
   function get_path() {
    return $this->user_path;
   }
}

$user_data = unserialize($_GET['data']);
$user = new UserClass("agreement.doc", "/tmp/");
echo $user->get_doc();
echo "<br>";
echo $user->get_path();
?>
```
 
-----SPLIT-----
 
# Answer

It is a Deserialization issue. The example shows a PHP class with an exploitable 'destruct' method. An attacker might be able to delete an arbitrary file via a Path Traversal attack, for e.g. requesting the following URL: http://testsite.com/vuln.php?data=O:8:"Example1":1:{s:10:"cache_file";s:15:"../../index.php";} - https://owasp.org/www-community/vulnerabilities/PHP_Object_Injection
