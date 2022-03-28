# Question
 
What is the problem here?
 
```
public static void main(String[] args) throws Exception {
    System.out.println("The folder name you want to create is: " + args[0]);
    String folderName = args[0];
    String cmd = "mkdir " + folderName;
    Runtime.getRuntime().exec(cmd);
}
```
 
-----SPLIT-----
 
# Answer

It is a Code Execution issue. 'folderName' parameter is vulnerable to OS command injection attacks. An intruder can supply 'FolderName; id' input to run consecutive commands.