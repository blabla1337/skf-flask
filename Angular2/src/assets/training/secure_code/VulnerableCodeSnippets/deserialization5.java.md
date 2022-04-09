# Question
 
What is the problem here?
 
```
protected void processUploadedFiles(String filePath) {
  System.out.println("Your file is being processed now!");
  FileInputStream fileInput = new FileInputStream(filePath);
  ObjectInputStream objectInput = new ObjectInputStream(fileInput);
  Object obj = objectInput.readObject();
}
```
 
-----SPLIT-----
 
# Answer

It is a Deserialization issue. 'fileInput' file content is not being checked before processing and directly deserialization of user supplied data may cause security issues.
