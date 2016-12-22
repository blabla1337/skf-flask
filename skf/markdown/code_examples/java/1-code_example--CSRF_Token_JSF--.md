




/*
<html xmlns="http://www.w3.org/1999/xhtml"
    xmlns:h="http://java.sun.com/jsf/html"
        xmlns:f="http://java.sun.com/jsf/core"
	    xmlns:p="http://primefaces.org/ui"
	        xmlns:cu="http://localhost:8080/custom"
		    xmlns:ui="http://java.sun.com/jsf/facelets">
		     
		      <f:view contentType="text/html">
		       
		      <f:event listener="#{userLoginView.isAuthenticated}" type="preRenderView" />

[ .... ] 

      
              <p:commandButton action="password?faces-redirect=true" value="Add User" ajax="false">
                	<cu:antiCSRF/>
		</p:commandButton>
		          </h:form>
[ .... ]


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
