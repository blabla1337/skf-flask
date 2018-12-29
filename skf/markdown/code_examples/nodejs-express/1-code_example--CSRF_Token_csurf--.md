# CSRF Tokens - JSF
-------

## Example:

	/*
	General:
	If you're using JSON  over REST to mutate server state and the application doesn't support plain HTML form submissions and your CORS configuration bans cross-domain requests then Express has built-in CSRF protection.
	If you support plain HTML form submissions, read on.
	Hint: you can check if you support plain HTML form submissions by searching for:
	require("body-parser"); and
	bodyParser.urlencoded()
	*/

	/*

	The following handlebar template snippet shows the code used to place the antiCSRF token inside the page.
	When the page renders, the <cu:antiCSRF/> is created as a viewstate encoded html input tag
	which then carries the antiCSRF token.
	While in process of rendering the page, a new token is generated
	and added into the existing session.
	When the user press the commandButton
	then CSRF token parameter is compared with the CSRF session parameter. 

	*/

	/*
	<form action="/process" method="POST">
    	<input type="hidden" name="_csrf" value="{{csrfToken}}">
    	[...]
    	<button type="submit">Submit</button>
	</form>
	*/
	 
	//	the following snippet is used to generate and check the token. 
	var csrf = require('csurf')    //csrf module
	var csrfProtection = csrf({ cookie: true }) // setup route middlewares

	// Error handler(Optional) shows custom error message
	// when token is missing or mismatches
	app.use(function (err, req, res, next) {
		// on token validation fail, error is thrown with
		// code 'CSRFERROR'
		if (err.code !== 'CSRFERROR') return next(err);
			res.status(403);
			res.send('csrf error');
		});

	//  we need to pass the middleware to each view 
	app.get('/form', csrfProtection, function(req, res) {
  		// generate and pass the csrfToken to the view
	  res.render('send', { csrfToken: req.csrfToken() })
	})

	// and check it when the request is being processed  
	app.post('/process', parseForm, csrfProtection, function(req, res) {
  		res.send('data is being processed')
	})

	/* Considerations!! 
	csurf doens't protect by default requests such as GET, OPTIONS, HEAD.
	
	*/