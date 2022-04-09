# Question
 
What is the problem here?
 
```
<?php echo "Please type a file name you want to include"; ?>

<form action="index.php" method="GET">
    <input type="text" name="fileName">
</form>

<?php
   $file = str_replace('../', '', $_GET['fileName']);
   if(isset($file))
   {
       include("/var/www/$file");
   }
   else
   {
       include("index.php");
   }
?>
```
 
-----SPLIT-----
 
# Answer

It is a  Local File Inclusion(LFI) issue. 'fileName' parameter is not properly checked. Users can load any files they want with the service account privilege. You also see, the code replace '../' with nothing for a sanitization purpose, however attacker can bypass it with providing '..././' in the path.
