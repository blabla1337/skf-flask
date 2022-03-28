# Question
 
What is the problem here?
 
```
...
[Route("/uploadedFiles")]
public class FileAnalyser 
{
    [HttpGet("{binaryFile}")]
    public string analysisFiles(string binaryFile)
    {
        Process proc = new Process();
        proc.StartInfo.FileName = binaryFile;
        proc.StartInfo.RedirectStandardOutput = true;
        proc.Start();
        string output = proc.StandardOutput.ReadToEnd();
        proc.Dispose();
        return output;
    }
}
```
 
-----SPLIT-----
 
# Answer

It is a Code Execution issue. 'binaryFile' parameter is vulnerable to OS command injection attacks. An intruder can supply OS command delimeters (;,|,&, etc) to run consecutive commands.