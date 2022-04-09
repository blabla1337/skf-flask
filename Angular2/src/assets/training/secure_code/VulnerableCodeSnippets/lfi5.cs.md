# Question
 
What is the problem here?
 
```
private const string notepadFolder = @"C:\Users\Personal\Notes\"; 
[HttpGet("{fileName}")]
public void personalNotepad(string fileName){
    Console.WriteLine("Your notepad file name will be " + fileName);
    Console.WriteLine("What notes you want to save:");
    string userNotes = Console.ReadLine();
    using var contentSaver = new StreamWriter(notepadFolder + userInput);
    contentSaver.WriteLine(userNotes);
    Console.WriteLine("Saved!");
}
```
 
-----SPLIT-----
 
# Answer

It is a  Local File Inclusion(LFI) issue. 'fileName' parameter is not sanitized for injections properly. Therefore, the user can over-write other OS files and modify contents.
