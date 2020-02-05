# Logout 
-------

## Example:


	package com.edw;

	import java.io.IOException;
	import javax.servlet.ServletException;
	import javax.servlet.annotation.WebServlet;
	import javax.servlet.http.Cookie;
	import javax.servlet.http.HttpServlet;
	import javax.servlet.http.HttpServletRequest;
	import javax.servlet.http.HttpServletResponse;

	/*
	- Servlet implementation class Logout
	*/
	@WebServlet("/Logout")
	public final class Logout extends HttpServlet {
		private static final long serialVersionUID = 1L;
		
		/**
		* @see HttpServlet#HttpServlet()
		*/
		public Logout() {
			super();
		}

		/**
		* @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
		*/
		protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
			response.getWriter().append("Served at: ").append(request.getContextPath());
		}

		/**
		* @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
		*/
		protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
			
			request.getSession().invalidate();
			request.getSession().setAttribute("Authenticated", "");
			
			Cookie cookie = null;
			Cookie[] cookies = null;
			// Get an array of Cookies associated with this domain
			cookies = request.getCookies();
				
			for (Cookie cookie2 : cookies) {
				cookie = cookie2;
				
				if (cookie.getName().equals("JSESSIONID"))
				{        	 
					cookie.setValue("");
				}
			
				response.addCookie(null);
				request.setAttribute("msg","Session terminated!");
				request.getRequestDispatcher("/login.jsp").forward(request, response);
				return;
			}
		}
	}
