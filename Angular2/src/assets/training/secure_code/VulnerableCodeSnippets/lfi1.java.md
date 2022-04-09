# Question
 
What is the problem here?
 
```
public static void main(String[] args) throws Exception {
    System.out.println("The URL address of the file you want to display in here is " + args[0]);
    URL path = new URL(args[0]);
    BufferedReader read = new BufferedReader(
    new InputStreamReader(path.openStream()));
    String i;
    while ((i = read.readLine()) != null)
        System.out.println(i);
    read.close();
}
```
 
-----SPLIT-----
 
# Answer

It is a  Local File Inclusion(LFI) issue. The argument is not being checked properly and intruders can load also local files, besides web requests.
