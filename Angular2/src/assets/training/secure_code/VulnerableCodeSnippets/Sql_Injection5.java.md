# Question
 
What is the problem here?
 
```
try (var connection = dataSource.getConnection()) {
    PreparedStatement statement = connection.prepareStatement("select password from challenge_users where userid = '" + username_login + "' and password = '" + password_login + "'");
    ResultSet resultSet = statement.executeQuery();
    if (resultSet.next()) {
        System.out.println("You have successfully logged in!");
    } else {
        System.out.println("Please provide a valid credentials!");
    }
}
```
 
-----SPLIT-----
 
# Answer

It is an SQL Injection issue. 'username_login' and ' password_login' parameters are vulnerable for malicious injection and no input sanitization takes place. And additionally, the code shows a wrong implementation of 'PreparedStatement'.