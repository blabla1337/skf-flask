# Question
 
What is the problem here?
 
```
private const String fileDownloadPath = @"C:\Temp\";
[HttpGet("{fileNametoDelete}")]
public void fileRemover(string fileNametoDelete){   
    fileNametoDelete = fileNametoDelete.Replace("..\\", "");
    Console.WriteLine("The file will be removed permanently: " + fileNametoDelete);
    try
    {
        var fullPath = Path.Combine(fileDownloadPath, fileNametoDelete);
        System.IO.File.Delete(fullPath);
    }    
    catch (IOException ioExp)    
    {    
        Console.WriteLine("An error occurred when deleting the file!");    
    }
    Console.ReadKey();
}
```
 
-----SPLIT-----
 
# Answer

It is a  Local File Inclusion(LFI) issue. 'fileNametoDelete' parameter is not properly checked. Users can delete any files they want with the service account privilege. You also see, the code replace '..\\' with nothing for a sanitization purpose, however attacker can bypass it with providing '...\\.\\' in the path.
