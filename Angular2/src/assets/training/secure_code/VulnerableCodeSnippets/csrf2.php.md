# Question
 
What is the problem here?
 
```
<?php 
    if (isset($_GET['signPetitionForm'])) { 
        $userName = $_GET['userName']; 
        $userName = stripslashes($userName); 
        $userName = mysql_real_escape_string($userName); 

        $userComment = $_GET['userComment']; 
        $userComment = stripslashes($userComment); 
        $userComment = mysql_real_escape_string($userComment); 

        $insert="UPDATE `petitionform` SET userComment = '$userComment' WHERE userName = '$userName';"; 
        $result=mysql_query($insert) or die('<H3>No record or a problem has occurred</H3>'); 

        echo "<pre> Thank you for your support. Your form has been signed! </pre>";         
        mysql_close(); 
    } 
?>
```
 
-----SPLIT-----
 
# Answer
 
It is a Cross-Site Request Forgery (CSRF) issue. 'userName' and 'userComment' are sanitized properly, however there is no anti-CSRF token control takes place. A malicious link can make victim's session to execute tasks.
