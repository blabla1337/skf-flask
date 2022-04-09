# Question
 
What is the problem here?
 
```
...
protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws IOException {
      doGet(req, resp); 
}
public CachedRowSetImpl getUser(Connection con, String userID) throws SQLException {
  CachedRowSetImpl crs = null;
  PreparedStatement preState = null;
  String query = "select * from USERS where userID=?";
  try {
    preState = con.prepareStatement(query);
    preState.setString(1, userID);
    ResultSet rs = preState.executeQuery();
    crs = new CachedRowSetImpl();
    crs.populate(rs);
    return crs;
  }
}
protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
    String userName = req.getParameter("userName");
    PrintWriter out = resp.getWriter();
    out.write("Hello " + userName);
}
```
 
-----SPLIT-----
 
# Answer

It is a Cross Site Scripting (XSS) issue. 'userName' parameter is vulnerable for injection attacks and no input sanitization exists. Injected javascript codes will be executed in the response. On the other hand, the database query looks fine.
