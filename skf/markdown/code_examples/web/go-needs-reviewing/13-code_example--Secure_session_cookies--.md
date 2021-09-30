# Secure session cookies
-------

## Example:


	// By setting the Secure attribute to true you can have your cookies 
	// encrypted in transit to avoid "man-in-the-middle" attacks

	func ExampleHandler(w http.ResponseWriter, r *http.Request) {
		cookie := &http.Cookie{
			Name:  "mycookie",
			Value: "mycookievalue",
			Path: "/",
			Domain: "acme.domain.com",
			MaxAge: 60000,
			Expires: time.Now().AddDate(0, 0, 1),
			Value: strconv.FormatInt(time.Now().Unix(), 10),
			HttpOnly: true,
			SameSite: http.SameSiteStrictMode,
			// When creating the cookie ensure Secure is set to true
			Secure: true,
		}

		// http://golang.org/pkg/net/http/#SetCookie
		http.SetCookie(w, cookie)
	}
