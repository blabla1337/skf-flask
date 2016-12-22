CSRF Tokens - JSF
-----------------

 
***Example:***


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

/*

After a successful validation of a user login, the application must also start a session
which contains the "cross site request forgery" token.

The following .xhtml snippet shows the code used to plase the antiCSRF token inside the page.
when the page renders the <cu:antiCSRF/> is an html input tag which carries the antiCSRF
token and is been constructed dynamically. When the page renders , a new token is generated
explicitly and then adds the new value into the session. When the User push the commandButton
then the input tag CSRF token parameter is compared with the CSRF session parameter. 

*/


/*
          <f:view contentType="text/html">    
          <f:event listener="#{userLoginView.isAuthenticated}" type="preRenderView" />
[ .... ]

          <p:commandButton action="password?faces-redirect=true" value="Add User" ajax="false">
                <cu:antiCSRF/>
    </p:commandButton>
              </h:form>

[ .... ]

/* 

the following function is used to generate the new Session which then is added to the already existing session. 

*/


public void generateToken(){
		
		HttpServletRequest origRequest = (HttpServletRequest)FacesContext.getCurrentInstance().getExternalContext().getRequest();

    	//we include the random password/token class.
  	    randomizer CSRF = new randomizer();
		 /*
        Now we create a random value for our CSRF tokens. See "Random password token generation" in
        the code examples for more detailed information:
        */
        String CSRftoken = CSRF.generate(25);
                
        //Set an accesor session.
        origRequest.getSession(false);
        origRequest.getSession().setAttribute("CSRF", CSRftoken);
	}

/* 
the following function is been used to do the comparison between the CSRF token coming from the
input tag and the CSRF value coming from the session 
*/

    public void antiCSRF() throws IOException
    {		
        HttpServletRequest origRequest = (HttpServletRequest)FacesContext.getCurrentInstance().getExternalContext().getRequest();
        HttpServletResponse origResponse = (HttpServletResponse)FacesContext.getCurrentInstance().getExternalContext().getResponse();
        String AUTH_KEY =  (String) FacesContext.getCurrentInstance().getExternalContext().getSessionMap().get("AUTH_KEY");
       	FacesContext.getCurrentInstance().getExternalContext().getSessionMap().remove(AUTH_KEY);
   		FacesContext.getCurrentInstance().getExternalContext().invalidateSession();
   		Cookie cookie = null;
   		Cookie[] cookies = null;
   	    // Get an array of Cookies associated with this domain
   	    cookies = origRequest.getCookies();		         
   		for (Cookie cookie2 : cookies) 
   		{
   			cookie = cookie2;		         
   				if (cookie.getName().equals("JSESSIONID"))
   				{        	 
	   				cookie.setValue(null);	       		
	   				origResponse.addCookie(cookie);
	   			
	                Log.SetLog("", "", "Cookie has been desroyed!", "", "NULL");    
   				} 
   		}		     
    }

/* 
This function is used to decode the viewstate of the jsf component into html input tag in order to get the parameter
and do some extra  processing. 
*/ 
		public void decode(FacesContext context) {
			 FacesContext fc = FacesContext.getCurrentInstance();

			// access the hidden input field value
			ExternalContext external = context.getExternalContext();
			Map<?, ?> requestMap = external.getRequestParameterMap();
			String value = String.valueOf(requestMap.get("_CSRFToken"));

			// access the session and get the token
			HttpSession session = (HttpSession) context.getExternalContext().getSession(false);
			String token = (String) session.getAttribute("CSRF");

			// check if the token exists
			if (value == null || "".equals(value)) {
				try {
					this.antiCSRF();
				} catch (IOException e) {
					logger.error(e.toString());
				}
				Log.SetLog("", "", "antiCSRF token doesnt match! Failed attempt", "", "NULL"); 
				logger.info("antiCSRF token doesnt match! Failed attempt");
				ConfigurableNavigationHandler nav = (ConfigurableNavigationHandler) fc.getApplication().getNavigationHandler(); 
    			nav.performNavigation("csrf");
			}

			// check the values for equality
			if (!value.equalsIgnoreCase(token)) {
				try {
					this.antiCSRF();
				} catch (IOException e) {
					logger.error(e.toString());
				}
				Log.SetLog("", "", "antiCSRF token doesnt match! Failed attempt", "", "NULL"); 
				logger.info("antiCSRF token doesnt match! Failed attempt");
				ConfigurableNavigationHandler nav = (ConfigurableNavigationHandler) fc.getApplication().getNavigationHandler(); 
    			nav.performNavigation("UserLogin");
			}

		}

/*
the following function is used to encode into a viewstate the html tag into a jsf component 
*/ 

	    @Override public void encodeEnd(FacesContext context) throws IOException 
	    {
	    	//generate new token in every request
	    	this.generateToken();
	    	// get the session (don't create a new one!)
	    	HttpSession session = (HttpSession) context.getExternalContext().getSession(false);
	    	// get the token from the session
	    	String token = (String) session.getAttribute("CSRF");
	    	// write the component HTML to the response
	    	ResponseWriter responseWriter = context.getResponseWriter();
	    	responseWriter.startElement("input", null);
	    	responseWriter.writeAttribute("type", "hidden", null);
	    	responseWriter.writeAttribute("name", "_CSRFToken", "");
	    	responseWriter.writeAttribute("value", token, "CSRF");
	    	responseWriter.endElement("input");
	    }

*/

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~