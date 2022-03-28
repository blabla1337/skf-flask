# Question
 
What is the problem here?
 
```
public void ban2IPAddress(HttpServletRequest request) {
  String ip = request.getParameter("ip");
  try {
    getJDBCConnection().createStatement().execute("INSERT INTO banned_ip(id, ip) VALUE('" + UUID.randomUUID().toString() + "','" + ip + "')");
  } 
  catch (SQLException exception) {
    exception.printStackTrace();
  }
  System.out.print("IP address error!");
}
```
 
-----SPLIT-----
 
# Answer

It is an SQL Injection issue. 'ip' parameter is vulnerable for malicious injection and no input sanitization or parameterized query takes place.