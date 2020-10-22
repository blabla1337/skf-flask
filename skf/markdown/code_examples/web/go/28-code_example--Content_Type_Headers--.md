Content-Type Headers
-------

## Example:

	const (
	  ContentTypeHeader = "Content-Type:text/html"
	  ContentTypeValue  = "charset=UTF-8"
	)

	func ExampleHandler(w http.ResponseWriter, r *http.Request) {
	  // Add Content-Type header
	  w.Header().Add(ContentTypeHeader, ContentTypeValue)

	  // Respond with request
	  w.Write([]byte("I have a Content-Type of text/html in UTF-8!"))
	}
