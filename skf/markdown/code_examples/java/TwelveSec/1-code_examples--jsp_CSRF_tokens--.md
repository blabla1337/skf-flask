

JSP-Servlets
-------------------------

### Cross Site request Forgery 


> For CSRF tokens we used a separate class outside of the normal controller, since
> it must be re-used on several locations throughout the application

> First after a successful validation of a user login, the application must also start a session
> which contains the "cross site request forgery" token.

> For generating the token we want to use a secure cryptographic function

```SecureRandom csprng = new SecureRandom();```

> Then we generate a long value token containing a high entropy

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
byte[] randomBytes  = new byte[128];

csprng.nextBytes(randombytes);
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

> Then we base64 encode the string

```String csrftoken = Base64.getEncoder().encodeToString(randomBytes);```

> Then we add a HttpSession session attribute

```session.setAttribute( "CSRF", csrftoken);```

> The next step is implementing this random token in each form field as a hidden input parameter
> and send it to a function which checks if the submitted token is equal to the one set after succesful validation.

```
    Object token = request.getSession().getAttribute("CSRF");
    String tokenStr = "";
    if (token != null) {
        tokenStr = (String) token;
    }

    System.out.println("+tokenStr " + tokenStr);

<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
Welcome to the OWASP CSRFGuard Test Application!
    <br />
    <form action="/Home/csrf" method="post">
        <input type="text" name="testValue" /> 
			<br/> 
			<input type="hidden" value="<%=tokenStr%>" name="token" />
			<input type="submit" value="login">
		</form>
```

> We use the following controller in order to take the csrf parameter and compare it with the session attribute 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
package com.edw;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;



import javax.servlet.http.HttpServletResponse;


@WebServlet("/CheckCSRF")
public class CheckCSRF extends HttpServlet {
	private static final long serialVersionUID = 1L;
       

    public CheckCSRF() {
        super();
        // TODO Auto-generated constructor stub
    }

    //here we are sending the token towards the function which does the token validation    
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		
		String token = request.getParameter("token");
		String Sessiontoken = (String) request.getSession().getAttribute("CSRF");

		
		if(Sessiontoken != token)
	    { 

		/*
        If there was no match the authentication session will be emptied and sessions
        Will be abandoned, we redirect the user towards the login page.
        */		
			if (request.getSession().getAttribute("authenticateUser") == "")
				{
				request.getSession().invalidate();
				request.setAttribute("msg", "Served at: " + request.getContextPath());
				RequestDispatcher rd =  request.getRequestDispatcher("/login");
			    rd.forward(request, response);
			    return;
				}
	    }	
	}

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		super.doGet(request, response);
	}

}

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
