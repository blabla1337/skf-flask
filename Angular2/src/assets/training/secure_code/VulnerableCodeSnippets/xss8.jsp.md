# Question
 
What is the problem here?
 
```
<%...
     Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/db","root","root"); 
    String query = "select * from emp where id=?";
    PreparedStatement preState = con.prepareStatement(query);
    preState.setString(1, userID);
    ResultSet rs = preState.executeQuery();
    if (rs != null) {
        rs.next();
    String name = rs.getString("userName");
%>

Employee Name: <%= userName %>
```
 
-----SPLIT-----
 
# Answer

It is a Cross Site Scripting (XSS) issue. 'userName' parameter is vulnerable for injection attacks and the code does not sanitize the user inputs properly. On the other hand, the database query looks fine.
