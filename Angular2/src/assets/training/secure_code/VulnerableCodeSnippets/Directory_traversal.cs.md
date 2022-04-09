# Question
 
What is the problem here?
 
```
private const string RootFolder = @"C:\Users\Temp\";         
public void Test(string fileName, string[] fileContent){
    using var outputFile = new StreamWriter(RootFolder + fileName);
    foreach (var line in fileContent)
        outputFile.WriteLine(line);
}
```
 
-----SPLIT-----
 
# Answer

It is a  Directory traversal issue. 'fileName' parameter is not sanitized properly. Client users can over-write any OS files with the content she/he provides with the privileges of the service account.
