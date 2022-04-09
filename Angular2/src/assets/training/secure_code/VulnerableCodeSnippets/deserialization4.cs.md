# Question
 
What is the problem here?
 
```
public String typeProcessor(string typeName, DbContext context, String filePath)  {
   String result = "Please provide a valid type!";
   var sqlQuery = "SELECT * FROM userTypes";
   if  (context.Database.ExecuteSqlCommand(sqlQuery) > 0)
   {   
      FileStream fs = new FileStream(filePath, FileMode.Open);
      Type t = Type.GetType(typeName);
      XmlSerializer serializer = new XmlSerializer(t);
      ExpectedType obj = (ExpectedType) serializer.Deserialize(fs);
      result = "Your request has been processed!";
      }
   return result;
}
```
 
-----SPLIT-----
 
# Answer

It is a Deserialization issue. 'typeName' is not being sanitized properly for serialization process and directly deserialize of user supplied data may cause this kind of issues. On the other hand, Sql query does not require any input for execution and therefore no injection is possible.
