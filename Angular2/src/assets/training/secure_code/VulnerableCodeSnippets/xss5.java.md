# Question
 
What is the problem here?
 
```
protected void doGet(HttpServletRequest req, HttpServletResponse res) throws IOException {
  String userName = req.getParameter("userName").replace("script", "");
  PrintWriter response = res.getWriter();
  response.write("Hello " + userName);
}
```
 
-----SPLIT-----
 
# Answer

It is a Cross Site Scripting (XSS) issue. 'userName' parameter is vulnerable for injection attacks and no a proper input sanitization exists. You may notice, the code replaces 'script' with nothing, however attacker can bypass it with sending 'scrscriptipt' for 'script'.
