# Question
 
What is the problem here?
 
```
public IActionResult login(String userName, String userPasswd, DirectoryEntry directoryEntry){
    DirectorySearcher directorySearcher = new DirectorySearcher(directoryEntry);
    directorySearcher.Filter = "(&(uid=" + userName + ")(userPassword=" + userPasswd + "))";
    return Content(directorySearcher.FindOne() != null ? "success" : "fail");
}
```
 
-----SPLIT-----
 
# Answer

It is an LDAP Injection issue. 'userName' and 'userPasswd' parameters are not being checked for any malicious injectins. The attacker can bypass login screen with a crafted request.
