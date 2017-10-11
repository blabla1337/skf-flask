X-XSS-Protection Header
-------

## Example:

	const (
	  XSSProtectionHeader = "X-XSS-Protection"
	  XSSProtectionValue  = "1; mode=block"
	)

	func ExampleHandler(w http.ResponseWriter, r *http.Request) {
	  // Add X-XSS-Protection header
	  w.Header().Add(XSProtectionHeader, XSSProtectionValue)

	  // Respond with request
	  w.Write([]byte("Hello World."))
	}
