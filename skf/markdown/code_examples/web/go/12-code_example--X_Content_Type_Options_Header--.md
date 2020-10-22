X-Content-Type-Options Header
-------

## Example:

	const (
	  ContentTypeOptionsHeader = "X-Content-Type-Options"
	  ContentTypeOptionsValue  = "nosniff"
	)

	func ExampleHandler(w http.ResponseWriter, r *http.Request) {
	  // Add X-Content-Type-Options header
	  w.Header().Add(ContentTypeOptionsHeader, ContentTypeOptionsValue)

	  // Respond with request
	  w.Write([]byte("I have X-Content-Type-Options header set to nosniff!"))
	}
