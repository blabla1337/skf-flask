CSRF Tokens - JSF
-----------------

 
***Example:***


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

/*

For CSRF tokens we used a separate class outside of the normal controller, since
it must be re-used on several locations throughout the application

After a successful validation of a user login, the application must also start a session
which contains the "cross site request forgery" token.

From the randomizer class we are generating the token we want by using a secure cryptographic function
SecureRandom csprng = new SecureRandom();

Then we generate a long value token containing a high entropy
byte[] randomBytes  = new byte[128];

csprng.nextBytes(randombytes);

Then we base64 encode the string
String csrftoken = Base64.getEncoder().encodeToString(randomBytes);

Then we set the session attribute.

origRequest.getSession(false);
origRequest.getSession().setAttribute("CSRF", CSRftoken);

The next step is to implement this random token in each form field as a hidden input parameter
and send it to a function which checks if the submitted token is equal to the one set after succesful validation.

The following .xhtml snippet shows the code used to place the antiCSRF token inside the page.
When the page renders, the <cu:antiCSRF/> is created as a viewstate encoded html input tag
which then carries the antiCSRF token.
While in process of rendering the page, a new token is generated
and added into the existing session. When the user press the commandButton
then CSRF token parameter is compared with the CSRF session parameter. 

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

the following function used to generate the new Session which then is added to the already existing session. 

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
the following function used to do the comparison between the CSRF token coming from the
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
This function used to decode the viewstate of the jsf component into html input tag in order to get the parameter
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
the following function used to encode into a viewstate the html tag into a jsf component 
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