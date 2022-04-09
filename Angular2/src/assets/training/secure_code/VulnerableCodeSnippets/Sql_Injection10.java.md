# Question
 
What is the problem here?
 
```
protected void doPost(HttpServletRequest request, HttpServletResponse response) {
    String username = request.getParameter("username");
    String password = request.getParameter("password");
    String query = "select * from USERS where user_name='" + username + "' and user_password = '" + password + "'";
    Connection conn = null;
    PreparedStatement stmt = null;
    try {
        conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/portalDB", "root", "p@$$w0rD");
        stmt = conn.prepareStatement(query);
        ResultSet rs = stmt.executeQuery();
        rs.close();
    } catch (Exception e) {} 
}
```
 
-----SPLIT-----
 
# Answer

It is an SQL Injection issue. 'username' and 'password' parameters are vulnerable spot. These parameters are being concatenated to build a SQL query without a proper sanitization. Also 'PreparedStatement' is implemented in a wrong way. A proper parameterization plays crucial role against SQL injections.
