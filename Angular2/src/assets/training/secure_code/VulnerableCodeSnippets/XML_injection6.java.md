# Question
 
What is the problem here?
 
```
public static void main(String args[]){  
  BufferedOutputStream outStream = new BufferedOutputStream(null);
  System.out.println("You are about to start author entries!");  
  String data = "<library>\n";
  String author, type, language;
  do
  {
    System.out.println("Author Name:");
    author = System.console().readLine();
    System.out.println("Author Type:");
    type = System.console().readLine();
    System.out.println("Author language:");
    language = System.console().readLine();
    data += "<author>" + author + "</author>\n";
    data += "<type>" + type + "</type>\n";
    data += "<language>" + language + "</language>\n";
    System.out.println("One more entry? Pleae type 'quit' to quit the app!");
    String input = System.console().readLine();
    if("quit".equals(input))
      break;
  } while (true);
  
  data += "</library>";
  System.out.println("\nYour file will be:\n\n"+ data);
  
  try {
      FileWriter fw = new FileWriter(new File("library.xml"));
      fw.write(data);
      fw.close();
  } catch (IOException iox) {}
  System.out.println("Your file has been saved!");
  System.console().readLine();
}
```
 
-----SPLIT-----
 
# Answer

It is an XML injection issue. 'author','type' and 'language' parameters are not being sanitized while building 'library.xml' file. The attacker can manipulate the file content.
