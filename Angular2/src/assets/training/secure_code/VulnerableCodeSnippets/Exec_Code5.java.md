# Question
 
What is the problem here?
 
```
public void healthChecker(String ippAdd){
  try{
    System.out.println("Pinging result of " + ippAdd);
    String cmd = request.getParameter("ping");
    Process process = Runtime.getRuntime().exec(cmd + " " + ippAdd);
    BufferedReader displayer = new BufferedReader(new displayerStreamReader(process.getdisplayerStream()));
    String line = null;
    while ((line = displayer.readLine()) != null) {
      System.out.println("Command output: " + line);
      }
    }
  catch (IOException e){  
    System.out.println("The target system can not be reachable!");
  } 
}
```
 
-----SPLIT-----
 
# Answer

It is a Command Injection issue. 'ippAdd' parameter is not sanitized properly and attacker can inject other OS commands to execute.