# Question
 
What is the problem here?
 
```
static void applicationLoginLogger(string userName, string task, string processDescription) {  
  logger.info("UserName: " + userName + ", task: " + task + ", processDescription: " + processDescription);
}
static boolean loginApplicatin(string userName, string userPasswd, Connection con) {
  PreparedStatement preState = null;
  try {
    preState = con.prepareStatement("select * from USERS where userName=? and userPasswd=?");
    preState.setString(1, userName);
    preState.setString(2, userPasswd);
    boolean result = preState.execute();
    
    if(result){
      applicationLoginLogger(userName, "Login Process", "Login Succeeded");
    }
    else{
      applicationLoginLogger(userName, "Login Process", "Login Failed");
    }
    return result;
  }
  catch(Exception e) {
    applicationLoginLogger(userName, "Login Process", "Login Failed");
    return False;
  }
}
```
 
-----SPLIT-----
 
# Answer

It is an CRLF injection issue. 'userName' is not being sanitized properly before processing. If the attacker uses 'CR' or 'LF' characters in the parameter, she/he can manipulate log files. For example: 'Record1 - User1\r\nAnotherRecord - OtherUser'.