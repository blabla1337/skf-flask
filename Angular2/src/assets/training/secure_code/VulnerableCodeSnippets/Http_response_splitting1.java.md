# Question
 
What is the problem here?
 
```
protected void doPost(HttpServletRequest req,HttpServletResponse res)throws ServletException,IOException{
	String student_name = req.getParameter("student_Name");
	if authorValidation(student_name){
		Cookie cookie = new Cookie("Student", student_name);
		cookie.setMaxAge(6000);  
		response.addCookie(cookie);
	}
	else {
	//no such student
	}
}
public boolean authorValidation(String student_name)
{
	//check if student exists
	...
}
```
 
-----SPLIT-----
 
# Answer

It is a Http Response Splitting issue. The code does not perform any sanitization for 'student_name' parameter. If the attacker provides 'CR' or 'LF' characters to the parameter, she/he can manipulate the service responses. For example: 'Name1\r\nContent-Length:40\r\n\r\n'