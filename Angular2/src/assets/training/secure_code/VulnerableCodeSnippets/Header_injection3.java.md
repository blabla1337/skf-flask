# Question
 
What is the problem here?
 
```
public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
	String clientIpAddress = request.getHeader("Client-IP: 127.0.0.1");
	if (clientIpAddress == null) {  
   		response.sendRedirect("/403.html");
	}
	else{
  		response.sendRedirect("/admin.html");
	}
}
```
 
-----SPLIT-----
 
# Answer

It is a Header Injection issue. 'clientIpAddress' header parameter is vulnerable for manipulation. Attacker can provide any 'Client-IP' address to bypass the restrictions.
