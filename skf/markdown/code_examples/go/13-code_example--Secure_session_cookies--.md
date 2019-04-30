# Secure session cookies
-------

## Example:


    // Javascript cannot set or read a cookie's value if the HTTPOnly attribute is set.
    // It makes client side attacks such as Cross Site scripting harder to exploit,as the
    // attacker will not be able to steal the user's cookies.

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