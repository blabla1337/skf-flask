# SQL Query JDBC
-------

# Example:


/*
- The JDBC library provides an API for building SQL commands that sanitize untrusted data. Use the java.sql.PreparedStatement class properly to escape input strings and prevent SQL injection.
- This example uses a parametric query with a ? character as a placeholder for the argument, and also validates the length of the username argument, preventing an attacker from submitting an arbitrarily long user name.
*/

public void doPrivilegedAction(
  String username, char[] password
) throws SQLException {
  Connection connection = getConnection();
  if (connection == null) {
    // Handle error
  }
  try {
    String pwd = hashPassword(password);
 
    // Validate username length
    if (username.length() > 8) {
      // Handle error
    }
 
    String sqlString =
      "select * from db_user where username=? and password=?";
    PreparedStatement stmt = connection.prepareStatement(sqlString);
    stmt.setString(1, username);
    stmt.setString(2, pwd);
    ResultSet rs = stmt.executeQuery();
    if (!rs.next()) {
      throw new SecurityException("User name or password incorrect");
    }
 
    // Authenticated; proceed
  } finally {
    try {
      connection.close();
    } catch (SQLException x) {
      // Forward to handler
    }
  }
}


