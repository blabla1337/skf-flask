Anti Clickjacking Headers
-------

## Example:

The preferred method to prevent against clickjacking is to use "security headers".
There are three options for setting the "anti-clickjacking" headers in your application:

	const (
		XFrameOptionsHeader = "X-Frame-Options"
		XFrameOptionsDeny  = "DENY"
		XFrameOptionsSameOrigin = "SAMEORIGIN"
		XFrameOptionsFromUri = "FROMURI http://www.example.com"
	)

	func ExampleHandler(w http.ResponseWriter, r *http.Request) {

		// Prevent page from being displayed in an iframe
	  	w.Header().Add(XFrameOptionsHeader, XFrameOptionsDeny)

		// Prevent page from being displayed in an iframe on other sites
		// w.Header().Add(XFrameOptionsHeader, XFrameOptionsSameOrigin)

		// Allow page at specified URI to display page in an iframe
		// NOTE: Limited support in modern browsers
		// w.Header().Add(XFrameOptionsHeader, XFrameOptionsFromUri)

		// Respond with request
	  	w.Write([]byte("I have security headers!"))
	}
