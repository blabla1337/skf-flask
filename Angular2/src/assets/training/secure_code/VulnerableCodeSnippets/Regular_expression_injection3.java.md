# Question
 
What is the problem here?
 
```
public static void doYourOwnTroubleShoot(String userName) {
    System.out.println(userName + " related erros will be shown.");
    String regex = "(.*? +userlog\\[\\d+\\] +.*" + userName + ".*)";
    Pattern searchPattern = Pattern.compile(regex);
    try(BufferedReader inputFile= new BufferedReader(new FileReader("/var/log/logs.txt"))){
        String line;
        while((line = inputFile.readLine()) != null){
            Matcher m = searchPattern.matcher(line);
            if (m.find()){
                System.out.println("Log Record => " + line);
            }
        }
    }
    catch (Exception e){}
}
```
 
-----SPLIT-----
 
# Answer

It is a Regular Expression Injection issue. 'userName' is vulnerable spot in here and an attacker can bypass 'userlog' restriction and read whole file with only crating a malicious 'userName' value. Any user supplied data should be sanitized before processing.
