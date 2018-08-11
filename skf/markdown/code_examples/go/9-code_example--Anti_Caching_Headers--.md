Anti-caching Headers
-------

## Example:

	const (
	  CacheControlHeader = "Cache-Control"
		CacheControlValue = "no-cache, no-store, must-revalidate"
		PragmaHeader = "Pragma"
		PragmaValue = "no-cache"
		ExpiresHeader = "Expires"
		ExpiresValue = "0"
	)

	func ExampleHandler(w http.ResponseWriter, r *http.Request) {
	  // Add Cache-Control header
		// HTTP 1.1
	  w.Header().Add(CacheControlHeader, CacheControlValue)

		// Add Pragma header
		// HTTP 1.0
		w.Header().Add(PragmaHeader, PragmaValue)

		// Add Expires header
		// Proxies
		w.Header().Add(ExpiresHeader, ExpiresValue)

	  // Respond with request
	  w.Write([]byte("I have anti-caching headers!"))
	}
