# Session cookies (domain)
-------

## Example:

	import "net/http"

	func ExampleHandler(w http.ResponseWriter, r *http.Request) {
        cookie := &http.Cookie{
            Name:  "mycookie",
            Value: "mycookievalue",
            Path: "/",
            MaxAge: 60000,
            Expires: time.Now().AddDate(0, 0, 1),
            Value: strconv.FormatInt(time.Now().Unix(), 10),
			HttpOnly: true,
            Secure: true,
			SameSite: http.SameSiteStrictMode,
            
            // When creating the cookie ensure Domain is set to the subdomain or domain
			// explicitly for which parts your application needs to access it
			Domain: "your.domain.com",
        }
        // http://golang.org/pkg/net/http/#SetCookie
        http.SetCookie(w, cookie)
	}