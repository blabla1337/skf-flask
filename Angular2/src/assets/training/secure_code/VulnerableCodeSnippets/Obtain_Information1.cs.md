# Question
 
What is the problem here?
 
```
private const String saltFolder = @"C:\Users\Salts\";

public void userSaltFile(String userName, String passwdSalt){
    String passwdSaltFilePath = saltFolder + userName + ".txt";
    Console.WriteLine("Your personal salt value will be saved to: " + passwdSaltFilePath);
    using var saver = new StreamWriter(passwdSaltFilePath);
    saver.WriteLine(passwdSalt);
}

public void userCreate(String userName, String userPassword, Connection con){        
    Random rnd = new Random();
    String salt=rnd.Next().ToString();
    userSaltFile(userName, salt);
    String userHash = (userPassword + salt).GetHashCode();
    PreparedStatement preState = null;
    String query = "INSERT INTO users (userName, userPass) VALUES (?, ?);";
    preState = con.prepareStatement(query);
    preState.setString(1, userName);
    preState.setString(2, userHash);
    ResultSet rs = preState.executeQuery();
}
```
 
-----SPLIT-----
 
# Answer

It is an Obtain Information issue. The application exposes too much details to clients. The code shows personal salt file's path to end users, which is not necessary. On the other hand, SQL query looks legit with using prepared statements.
