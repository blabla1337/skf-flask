	# HTML output
	-------

	## Example:


	/*
	Whenever user input is displayed in the application, whether, as content or a parameter value
	submitted towards the url, all user input should be properly escaped to prevent XSS injections.

	Go has a built in package called template (html/template) that implements data-driven templates for generating HTML output safe against code injection. It provides the same interface as package text/template and should be used instead of text/template whenever the output is HTML.

	More information about how this package handles various contexts can be found in the godoc: https://pkg.go.dev/html/template

	It also defines a security model that expl
	*/

	package main

	import (
		"html/template"
		"log"
		"os"
	)

	func main() {
		check := func(err error) {
			if err != nil {
				log.Fatal(err)
			}
		}

		// Produces safe, escaped HTML output
		// Hello, &lt;script&gt;alert(&#39;you have been pwned&#39;)&lt;/script&gt;!
		t, err := template.New("foo").Parse(`{{define "T"}}Hello, {{.}}!{{end}}`)
		check(err)
		err = t.ExecuteTemplate(os.Stdout, "T", "<script>alert('you have been pwned')</script>")
		check(err)
	}
